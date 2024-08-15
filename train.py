#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import argparse
import os
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def train(args):
    train_data = pd.read_csv(os.path.join(args.train, 'train.csv'))
    X_train = train_data.drop('PRICE', axis=1)
    y_train = train_data['PRICE']
    
    model = RandomForestRegressor(max_leaf_nodes=args.max_leaf_nodes)
    model.fit(X_train, y_train)
    
    os.makedirs(args.model_dir, exist_ok=True)
    model_path = os.path.join(args.model_dir, 'model.joblib')
    joblib.dump(model, model_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN'])
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    parser.add_argument('--max-leaf-nodes', type=int, default=30)
    args = parser.parse_args()
    
    train(args)

