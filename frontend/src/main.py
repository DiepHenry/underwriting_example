import requests
import streamlit as st
import os

os.environ['NO_PROXY'] = '10.184.26.9'

st.title('Accelerated Underwriting Example')

gender = st.selectbox('Gender', ['Male', 'Female'])

issue_age = st.number_input('Issue Age', 18, 80, 30)

bmi = st.number_input('BMI', 10.0, 50.0, 24.5, 0.1)

if st.button('Submit'):
    url = 'http://10.184.26.9:80/predict'
    gender_binary = 0
    if gender == 'Female':
        gender_binary = 1
    data = {'gender': gender_binary, 'age': issue_age, 'bmi': bmi}
    resp = requests.post(url, json=data)
    st.write(resp.json())

