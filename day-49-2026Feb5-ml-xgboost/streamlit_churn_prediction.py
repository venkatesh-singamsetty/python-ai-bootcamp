import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.title("🏦 Bank Churn Predictor")

# Load necessary artifacts
path = os.path.dirname(__file__)
model = joblib.load(os.path.join(path, "xgboost_churn_model.joblib"))
ct = joblib.load(os.path.join(path, "preprocessor_ct.joblib"))
le = joblib.load(os.path.join(path, "label_encoder_gender.joblib"))

# Sidebar for inputs
with st.sidebar:
    st.header("Customer Details")
    geo = st.selectbox("Geography", ["delhi", "bangalore", "mumbai"])
    gen = st.selectbox("Gender", ["Male", "Female"])
    age = st.slider("Age", 18, 92, 35)
    score = st.number_input("Credit Score", 300, 850, 600)
    tenure = st.slider("Tenure", 0, 10, 5)
    balance = st.number_input("Balance ($)", 0.0, 300000.0, 50000.0)
    products = st.selectbox("Products", [1, 2, 3, 4])
    card = 1 if st.radio("Has Credit Card?", ["Yes", "No"]) == "Yes" else 0
    active = 1 if st.radio("Is Active Member?", ["Yes", "No"]) == "Yes" else 0
    salary = st.number_input("Salary ($)", 0.0, 200000.0, 75000.0)

# Prediction
if st.button("Predict Churn"):
    # Pre-process inputs
    gen_enc = le.transform([gen])[0]
    raw_data = np.array([[score, geo, gen_enc, age, tenure, balance, products, card, active, salary]])
    
    # Transform and force numeric type
    processed = ct.transform(raw_data)
    processed = np.array(processed, dtype=np.float32)
    
    # Predict
    prob = model.predict_proba(processed)[0][1]
    prediction = 1 if prob > 0.5 else 0
    
    # Results
    st.divider()
    if prediction == 1:
        st.error(f"⚠️ Likely to CHURN (Probability: {prob:.2%})")
    else:
        st.success(f"✅ Likely to STAY (Probability: {prob:.2%})")
    
    st.write("Summary:", pd.DataFrame({"Score": [score], "Geo": [geo], "Age": [age], "Prob": [f"{prob:.2%}"]}))
