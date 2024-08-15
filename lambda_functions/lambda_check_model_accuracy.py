#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import boto3
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import mean_squared_error

def lambda_handler(event, context):
    test_data = download_test_data()
    
    model = download_model_from_s3()
    
    X_test = test_data.drop('PRICE', axis=1)
    y_test = test_data['PRICE']
    
    predictions = model.predict(X_test)
    
    mse = mean_squared_error(y_test, predictions)
    
    accuracy = 1 - (mse / np.var(y_test))  
    
    if accuracy > 0.8:  
        return {
            'statusCode': 200,
            'body': f'Model accuracy is sufficient: {accuracy:.2f}. Proceeding to deployment.'
        }
    else:
        return {
            'statusCode': 400,
            'body': f'Model accuracy is insufficient: {accuracy:.2f}. No deployment will be done.'
        }

def download_test_data():
    s3 = boto3.client('s3')
    bucket_name = 'bucket1'
    file_name = 'test.csv'
    
    s3.download_file(bucket_name, file_name, '/tmp/test.csv')
    
    return pd.read_csv('/tmp/test.csv')

def download_model_from_s3():
    s3 = boto3.client('s3')
    bucket_name = 'bucket1'
    model_file = 'model/model.tar.gz'
    
    s3.download_file(bucket_name, model_file, '/tmp/model.tar.gz')
    
    return joblib.load('/tmp/model.joblib')

