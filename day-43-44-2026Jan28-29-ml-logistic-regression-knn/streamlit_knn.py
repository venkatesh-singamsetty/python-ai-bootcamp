import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.title("🤝 Social Ad Buy Predictor (KNN)")

# Load model and scaler
path = os.path.dirname(__file__)
model_path = os.path.join(path, "knn_model.joblib")
scaler_path = os.path.join(path, "scaler.joblib")

if not os.path.exists(model_path):
    st.error("Model artifacts not found. Please run 'logistic_classification_knn_model.py' first.")
    st.stop()

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# Sidebar inputs
st.sidebar.header("Customer Details")
age = st.sidebar.slider("Age", 18, 60, 30)
salary = st.sidebar.number_input("Estimated Salary ($)", 15000, 150000, 50000)

# Prediction logic
if st.button("Predict Purchase"):
    # Scale inputs
    input_data = scaler.transform([[age, salary]])
    
    # Predict
    prob = model.predict_proba(input_data)[0][1]
    prediction = 1 if prob > 0.5 else 0
    
    st.divider()
    if prediction == 1:
        st.success(f"💰 Customer is likely to PURCHASE (Probability: {prob:.2%})")
    else:
        st.error(f"❌ Customer is likely NOT to purchase (Probability: {prob:.2%})")
    
    st.write("Summary:", pd.DataFrame({"Age": [age], "Salary": [salary], "Prob": [f"{prob:.2%}"]}))
