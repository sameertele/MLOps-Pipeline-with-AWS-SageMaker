# MLOps Pipeline with AWS SageMaker

## Project Overview

This project sets up an end-to-end MLOps pipeline using AWS SageMaker to automate the workflow of data ingestion, feature engineering, model training, evaluation, and deployment. The pipeline also includes continuous model retraining and updating using AWS Step Functions. The **Boston Housing Prices** dataset from the `sklearn` library is used to predict house prices.

## Project Architecture

1. **Data Ingestion**: Load the dataset and upload it to Amazon S3.
2. **Feature Engineering**: Process the data (normalize, handle missing values, etc.) and upload the processed data to S3.
3. **Model Training**: Train the model using AWS SageMaker.
4. **Model Deployment**: Deploy the trained model as a SageMaker endpoint.
5. **Automation**: Use AWS Step Functions to automate the retraining and redeployment process.
6. **Lambda Functions**: Use AWS Lambda functions to trigger training, evaluate model accuracy, and deploy the model if accuracy meets the threshold.

## Dataset

The project uses the **Boston Housing Prices** dataset from `sklearn`. This dataset contains 13 features describing housing characteristics and a target variable representing the median house price.

You can download the dataset using `sklearn.datasets.load_boston()` and save it to CSV.
