#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sagemaker
from sagemaker.sklearn import SKLearn
import boto3

def main():
    s3_input = 's3://bucket1/train.csv'
    
    sagemaker_session = sagemaker.Session()
    role = 'arn:aws:iam::myaccountID:role/sagemakertasks'
    
    estimator = SKLearn(
        entry_point='train.py',
        role=role,
        instance_type='ml.m5.large',
        framework_version='0.23-1',
        sagemaker_session=sagemaker_session,
        hyperparameters={'max_leaf_nodes': 30}
    )
    
    estimator.fit({'train': s3_input})
    
    model_path = estimator.model_data
    print(f"Model saved to: {model_path}")

if __name__ == "__main__":
    main()

