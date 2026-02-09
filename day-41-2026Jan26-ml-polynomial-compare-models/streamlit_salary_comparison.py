import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.title("💰 Employee Salary Predictor (Multiple Models)")

# Load artifacts
path = os.path.dirname(__file__)
models = {
    "Linear Regression": joblib.load(os.path.join(path, "linear_model.joblib")),
    "Polynomial Regression (Deg 5)": joblib.load(os.path.join(path, "poly_model.joblib")),
    "SVR (Kernel Poly Deg 5)": joblib.load(os.path.join(path, "svr_model.joblib")),
    "KNN Regression (k=4)": joblib.load(os.path.join(path, "knn_model.joblib")),
    "Decision Tree": joblib.load(os.path.join(path, "dt_model.joblib")),
    "Random Forest": joblib.load(os.path.join(path, "rf_model.joblib"))
}
poly_feat = joblib.load(os.path.join(path, "poly_feat.joblib"))
scaler_X = joblib.load(os.path.join(path, "scaler_X.joblib"))
scaler_y = joblib.load(os.path.join(path, "scaler_y.joblib"))

# Sidebar inputs
st.sidebar.header("Experience Details")
level = st.sidebar.slider("Position Level", 1.0, 10.0, 6.5, step=0.1)

# Model selection
model_type = st.sidebar.selectbox("Select Regression Model", list(models.keys()))

# Prediction logic
if st.button("Predict Salary"):
    selected_model = models[model_type]
    
    if model_type == "Polynomial Regression (Deg 5)":
        input_data = poly_feat.transform([[level]])
        prediction = selected_model.predict(input_data)[0]
    elif model_type == "SVR (Kernel Poly Deg 5)":
        input_data = scaler_X.transform([[level]])
        pred_scaled = selected_model.predict(input_data)
        prediction = scaler_y.inverse_transform(pred_scaled.reshape(-1, 1))[0][0]
    else:
        prediction = selected_model.predict([[level]])[0]
        
    st.divider()
    st.success(f"🎊 Predicted Salary: **${prediction:,.2F}**")
    st.info(f"Basis Level: {level}")
