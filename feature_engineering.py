#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import boto3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def main():
    bucket_name = 'bucket1'
    file_name = 'boston_housing.csv'
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, file_name, file_name)
    
    df = pd.read_csv(file_name)
    
    X = df.drop('PRICE', axis=1)
    y = df['PRICE']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    train_data = pd.DataFrame(X_train_scaled, columns=X.columns)
    train_data['PRICE'] = y_train.values
    test_data = pd.DataFrame(X_test_scaled, columns=X.columns)
    test_data['PRICE'] = y_test.values
    
    train_data.to_csv('train.csv', index=False)
    test_data.to_csv('test.csv', index=False)
    
    upload_data_to_s3(bucket_name, 'train.csv')
    upload_data_to_s3(bucket_name, 'test.csv')

if __name__ == "__main__":
    main()

