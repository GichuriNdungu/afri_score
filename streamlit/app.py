import streamlit as st
import requests

# Streamlit UI
st.title('Credit Prediction')

# User input fields
age = st.number_input('Age', min_value=18, max_value=100, value=30)
month = st.selectbox('Month', ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'))
day = st.number_input('Day', min_value=1, max_value=31, value=1)
balance = st.number_input('Balance', min_value=0, max_value=100000, value=5000)
duration = st.number_input('Duration', min_value=0, max_value=1000, value=100)
pdays = st.number_input('Pdays', min_value=0, max_value=100, value=10)

# Predict button
if st.button('Predict'):
    # Prepare data for prediction
    data = {
        "age": age,
        "month": month,
        "day": day,
        "balance": balance,
        "duration": duration,
        "pdays": pdays
    }

    # Make a request to FastAPI endpoint
    url = 'http://localhost:8000/docs'  # Replace with your FastAPI server URL
    response = requests.post(url, json=data)

    # Display prediction result
    if response.status_code == 200:
        prediction = response.json()['prediction']
        st.success(f'Prediction: {prediction}')
    else:
        st.error('Failed to get prediction from server')
