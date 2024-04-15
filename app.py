#!/usr/bin/env python3
import streamlit as st
from sklearn import preprocessing
import pandas as pd 
import numpy as np
import json
import os
import tensorflow as tf
from joblib import load
from src.prediction import predict
from joblib import load
from tensorflow.keras.models import load_model

cwd = os.getcwd()
print(cwd)
model = load_model('models/model.h5')
encoder_dict = load('models/encoder_dict.joblib')
print(f'This is the encoder dictionary \n {encoder_dict}')
columns = ['age','job','balance', 'day', 'month', 'duration']

def main():
    st.title('Credit Allocation predictor')
    html_temp =""""
    <div style = "background:#02524; padding:10px">
    <h2 style ="color:white;text-align:center;">Credit Allocation Predictor </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    age = st.text_input("Age", "0")
    job = st.selectbox("job", ["unemployed", "services", "management", "blue-collar", "self-employed", "technician", "entreprenuer", "admin.", "student", "housemaid", "retired", "unknown"])
    month = st.selectbox("month", ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])
    marital = st.selectbox("Marital", ["single","maried","divorced"])
    # housing = st.selectbox('Housing', ['No', 'Yes'])
    # housing = 0 if housing == "No" else 1
    education = st.selectbox('Education', ['primary','secondary','tertiary','unknown'])
    contact = st.selectbox('Contact', ['cellular','unknown','telephone'])
    poutcome = st.selectbox('Poutcome', ['failure','other','success','unknown'])
    campaign = st.text_input("Campaign", "0")
    previous = st.text_input("Previous", "0")
    day = st.text_input("day", "0")
    balance = st.text_input("balance", "0")
    duration = st.text_input("duration", "0")
    pdays = st.text_input("pdays", "0")

    if st.button("Predict"):
        data = {'age': int(age), 'job':job, 'month': month, 'day':int(day), 'balance': int(balance), 'duration':int(duration), 'pdays': int(pdays), 'marital':marital,
                 'education':education, 'contact': contact, 'poutcome': poutcome, 'campaign': int(campaign), 'previous': int(previous)}
        print(data)
        df = pd.DataFrame([list(data.values())], columns=['age','job','month','day', 'balance','duration', 'pdays', 'marital', 'education', 'contact', 'poutcome', 'campaign', 'previous'])
        for cat in encoder_dict:
            for col in df.columns:
                le = preprocessing.LabelEncoder()
                if cat == col:
                    le = encoder_dict[cat]
                    le_classes = le.classes_.tolist()
                    le_classes.append('Unknown')
                    le.classes_ = np.array(le_classes)
                    for unique_item in df[col].unique():
                        if unique_item not in list(le.classes_):
                            df[col] = ['Unknown' if x == unique_item else x for x in df[col]]
                        df[col] = le.transform(df[col])
        print(f'this should be the transformed df\n {df}')
        features_list = df.values.tolist()
        features_array = np.array(features_list)
        print(features_array.dtype)
        output = predict(model, features_array)
        if output == 0:
            text ="No customer does not qualify for credit"
        else:
            text = "Yes, customer qualifies for credit"
        st.success(f"{text}")

if __name__=='__main__': 
    main()
