#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import boto3
import sagemaker

def main():
    sagemaker_session = sagemaker.Session()
    role = 'arn:aws:iam::myaccountID:role/sagemakertasks'
    
    predictor = sagemaker.sklearn.model.SKLearnModel(
        model_data='s3://your-s3-bucket-name/model/model.tar.gz',
        role=role,
        entry_point='inference.py',
        framework_version='0.23-1',
        sagemaker_session=sagemaker_session
    )
    
    predictor.deploy(instance_type='ml.m5.large', initial_instance_count=1)

if __name__ == "__main__":
    main()

