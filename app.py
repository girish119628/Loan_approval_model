import streamlit as st
import pickle
import numpy as np
import pandas as pd

#Load the trained model
with open('classifier.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Loan Approval Prediction")

#Inputs
no_of_dependents = st.selectbox("Dependents", ["0", "1", "2", "3", "4", "5"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
income_annum = st.number_input("Applicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Term (in Years)", min_value=0)
cibil_score = st.number_input("Cibil Score", min_value=0)
total_assets = st.number_input("Total Assets", min_value=0)

#Button for prediction
if st.button("Predict Loan Approval"):
    input_data = {
        'no_of_dependents': no_of_dependents,
        'education': education,
        'self_employed': self_employed,
        'income_annum': income_annum,
        'loan_amount': loan_amount,
        'loan_term': loan_term,
        'cibil_score': cibil_score,
        'total_assets': total_assets
    }

    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]

    st.success(f"Loan Status Prediction: {prediction}")