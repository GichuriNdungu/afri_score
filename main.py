#!/usr/bin/env python3

from fastapi import FastAPI
from pydantic import BaseModel 
from typing import List, Optional
import numpy as np
import pandas as pd 
import pickle 
import tensorflow as tf 
from sklearn import preprocessing
from src.prediction import predict
from joblib import load


# model load 
print("before loading the model")
model = load('models/model.joblib')
print('after loading the model')
encoded_dict = load('models/encoded_dict.joblib')

# class for input data

class Data(BaseModel):
    age: int
    month: str
    day: int
    balance: int
    duration: int
    pdays: int
# create an instance of FastApi class 
app = FastAPI()
# endpoint for prediction
@app.post("/predict")
async def predict_credit(data:Data):
    # convert incomeing data to df 
    data = data.dict()
    print(data)
    df = pd.DataFrame([list(data.values())], columns=['age','month','day', 'balance','duration', 'pdays'])
    cat_cols = ['month']
    for cat in encoded_dict:
        for col in df.columns:
            le = preprocessing.LabelEncoder()
            if cat == col:
                le = encoded_dict[cat]
                for unique_item in df[col].unique():
                    if unique_item not in le.classes_:
                        df[col] = ['unknown' if x == unique_item else x for x in df[col]]
                if 'unknown' not in le.classes_:
                    le.classes_ = np.append(le.classes_, 'unknown')
                df[col] = le.transform(df[col])
    
    features_list = df.values.tolist()
    features_array = np.array(features_list)
    output = predict(model, features_array)
    if output == 0:
        text= "No customer does not qualify for credit"
    else:
        text = "Yes, customer qualifies for credit"
    return {"prediction": text}
