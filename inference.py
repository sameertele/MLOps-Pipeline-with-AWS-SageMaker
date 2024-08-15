#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import joblib
import pandas as pd

def model_fn(model_dir):
    model = joblib.load(os.path.join(model_dir, 'model.joblib'))
    return model

def input_fn(request_body, request_content_type):
    if request_content_type == 'text/csv':
        return pd.read_csv(request_body, header=None)
    else:
        raise ValueError("This model only supports CSV input")

def predict_fn(input_data, model):
    predictions = model.predict(input_data)
    return predictions

