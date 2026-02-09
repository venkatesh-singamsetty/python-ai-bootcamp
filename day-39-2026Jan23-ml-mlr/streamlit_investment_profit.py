import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.title("💸 Investment Profit Predictor")

# Load model
path = os.path.dirname(__file__)
model_path = os.path.join(path, "investment_profit_model.pkl")

if not os.path.exists(model_path):
    st.error("Model file not found. Please run the training script first.")
    st.stop()

model = joblib.load(model_path)

# Sidebar inputs
st.sidebar.header("Investment Details")
rd_spend = st.sidebar.number_input("Digital Marketing (R&D) Spend", 0.0, 200000.0, 75000.0)
admin_spend = st.sidebar.number_input("Promotion (Admin) Spend", 0.0, 200000.0, 120000.0)
mkt_spend = st.sidebar.number_input("Research (Marketing) Spend", 0.0, 500000.0, 200000.0)
state = st.sidebar.selectbox("State", ["Bangalore", "Chennai", "Hyderabad"])

# Prediction logic
if st.button("Predict Profit"):
    # Create input dataframe with all dummy variables
    # Order: [DigitalMarketing, Promotion, Research, State_Bangalore, State_Chennai, State_Hyderabad]
    input_data = {
        'DigitalMarketing': [rd_spend],
        'Promotion': [admin_spend],
        'Research': [mkt_spend],
        'State_Bangalore': [1 if state == "Bangalore" else 0],
        'State_Chennai': [1 if state == "Chennai" else 0],
        'State_Hyderabad': [1 if state == "Hyderabad" else 0]
    }
    input_df = pd.DataFrame(input_data)
    
    # Predict
    prediction = model.predict(input_df)[0]
    
    st.divider()
    st.success(f"📈 Predicted Profit: **${prediction:,.2f}**")
    
    st.write("Input Summary:", input_df)
