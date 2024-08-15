#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import boto3

def lambda_handler(event, context):
    sagemaker_client = boto3.client('sagemaker')
    
    response = sagemaker_client.create_model(
        ModelName='boston-housing-model',
        PrimaryContainer={
            'Image': '382416733822.dkr.ecr.us-east-2.amazonaws.com/sagemaker-random-forest:latest',
            'ModelDataUrl': 's3://bucket1/model/model.tar.gz'
        },
        ExecutionRoleArn='arn:aws:iam::myaccountid:role/sagemakertasks'
    )
    
    endpoint_config_response = sagemaker_client.create_endpoint_config(
        EndpointConfigName='boston-housing-endpoint-config',
        ProductionVariants=[
            {
                'InstanceType': 'ml.m5.large',
                'InitialInstanceCount': 1,
                'ModelName': 'boston-housing-model',
                'VariantName': 'AllTraffic'
            }
        ]
    )
    
    endpoint_response = sagemaker_client.create_endpoint(
        EndpointName='boston-housing-endpoint',
        EndpointConfigName='boston-housing-endpoint-config'
    )
    
    return {
        'statusCode': 200,
        'body': endpoint_response
    }

