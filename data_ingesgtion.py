#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import boto3
from sklearn.datasets import load_boston
import pandas as pd

def upload_data_to_s3(bucket_name, file_name):
    s3 = boto3.client('s3')
    s3.upload_file(file_name, bucket_name, file_name)

def main():
    boston = load_boston()
    df = pd.DataFrame(boston.data, columns=boston.feature_names)
    df['PRICE'] = boston.target
    
    file_name = 'boston_housing.csv'
    df.to_csv(file_name, index=False)
    
    bucket_name = 'bucket1'
    upload_data_to_s3(bucket_name, file_name)

if __name__ == "__main__":
    main()

