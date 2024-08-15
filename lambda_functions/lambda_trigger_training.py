#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import boto3

def lambda_handler(event, context):
    sagemaker_client = boto3.client('sagemaker')
    
    response = sagemaker_client.create_training_job(
        TrainingJobName='boston-housing-training-job',
        AlgorithmSpecification={
            'TrainingImage': '382416733822.dkr.ecr.us-east-2.amazonaws.com/sagemaker-random-forest:latest',
            'TrainingInputMode': 'File'
        },
        RoleArn='your-sagemaker-role',
        InputDataConfig=[
            {
                'ChannelName': 'train',
                'DataSource': {
                    'S3DataSource': {
                        'S3DataType': 'S3Prefix',
                        'S3Uri': 's3://bucket1/train.csv',
                        'S3DataDistributionType': 'FullyReplicated'
                    }
                },
                'ContentType': 'text/csv'
            }
        ],
        OutputDataConfig={
            'S3OutputPath': 's3://bucket1/model'
        },
        ResourceConfig={
            'InstanceType': 'ml.m5.large',
            'InstanceCount': 1,
            'VolumeSizeInGB': 10
        },
        StoppingCondition={
            'MaxRuntimeInSeconds': 3600
        }
    )
    
    return {
        'statusCode': 200,
        'body': response
    }

