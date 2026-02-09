import streamlit as st
import pandas as pd
import joblib, os
import numpy as np

st.set_page_config(page_title="Car MPG Predictor", page_icon="🚗")
st.title("🚗 Car Fuel Efficiency Predictor")
st.markdown("Compare Linear, Ridge, and Lasso model predictions based on vehicle specs.")

# 1. Load Everything
path = os.path.dirname(__file__)
model_type = st.sidebar.selectbox("Select Algorithm", ["linear", "ridge", "lasso"])

# Check if artifacts exist
if not os.path.exists(os.path.join(path, "linear_model.joblib")):
    st.error("Model artifacts not found. Please run 'lasso_ridge_regularization.py' first to train the models.")
    st.stop()

# Use caching for better performance
@st.cache_resource
def load_artifacts(m_type):
    model = joblib.load(os.path.join(path, f"{m_type}_model.joblib"))
    sc_x = joblib.load(os.path.join(path, "scaler_x.joblib"))
    sc_y = joblib.load(os.path.join(path, "scaler_y.joblib"))
    return model, sc_x, sc_y

model, sc_x, sc_y = load_artifacts(model_type.lower())

# 2. User Inputs (Matching 8-feature Training)
st.sidebar.header("Vehicle Specifications")
cyl = st.sidebar.slider("Cylinders", 3, 8, 4)
disp = st.sidebar.slider("Displacement", 60.0, 500.0, 150.0)
hp = st.sidebar.slider("Horsepower", 40.0, 250.0, 100.0)
wt = st.sidebar.slider("Weight (lbs)", 1500, 5000, 3000)
acc = st.sidebar.slider("Acceleration (0-60 mph)", 8.0, 25.0, 15.0)
yr = st.sidebar.slider("Model Year (70-82)", 70, 82, 76)
origin = st.sidebar.selectbox("Origin (1:USA, 2:Europe, 3:Asia)", [1, 2, 3])
car_type = st.sidebar.radio("Car Type", [0, 1], format_func=lambda x: "Large (0)" if x==0 else "Small/Medium (1)")

# 3. Prediction
if st.button("Predict MPG"):
    # Create input array (order must be: cyl, disp, hp, wt, acc, yr, origin, car_type)
    input_data = np.array([[cyl, disp, hp, wt, acc, yr, origin, car_type]])
    
    try:
        # Scale inputs using fitted Scaler
        input_scaled = sc_x.transform(input_data)
        
        # Get prediction
        pred_scaled = model.predict(input_scaled)
        
        # Inverse transform to get actual MPG value
        prediction = sc_y.inverse_transform(pred_scaled.reshape(-1, 1))[0][0]
        
        st.divider()
        st.success(f"⛽ Predicted Fuel Efficiency: **{prediction:.2f} MPG**")
        st.info(f"Basis Model: {model_type.capitalize()} Regression")
        
    except ValueError as e:
        st.error(f"Error: {e}")
        st.warning("This usually happens if you updated the training script but haven't re-run it yet. Please run 'python lasso_ridge_regularization.py' to reset the scalers.")
