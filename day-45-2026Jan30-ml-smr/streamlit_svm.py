import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.title("🛡️ Social Ad Buy Predictor (SVM)")

# Load model and scaler
path = os.path.dirname(__file__)
model_path = os.path.join(path, "svm_rbf_model.joblib")
scaler_path = os.path.join(path, "scaler_std.joblib")

if not os.path.exists(model_path):
    st.error("Model artifacts not found. Please run 'svm_classification_model.py' first.")
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
    prediction = model.predict(input_data)[0]
    
    # SVC doesn't always have predict_proba unless initialized with probability=True
    # But we can still show the final decision.
    st.divider()
    if prediction == 1:
        st.success(f"💰 Customer is likely to PURCHASE")
    else:
        st.error(f"❌ Customer is likely NOT to purchase")
    
    st.write("Summary:", pd.DataFrame({"Age": [age], "Salary": [salary]}))
