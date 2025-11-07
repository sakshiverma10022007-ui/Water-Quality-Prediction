import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("models/water_quality_model.pkl")

# App title
st.title("💧 Drinking Water Quality Prediction App")

st.write("""
This app predicts **Water Quality Safety** based on chemical and physical parameters.
Just enter the data below and click *Predict Quality*.
""")

# Create input fields
fluoride = st.number_input("Fluoride (mg/L)", min_value=0.0, max_value=5.0, step=0.1)
turbidity = st.number_input("Turbidity (NTU)", min_value=0.0, max_value=20.0, step=0.1)

# Add more fields if needed (based on your dataset)
ph = st.number_input("pH Value", min_value=0.0, max_value=14.0, step=0.1)
temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, step=0.1)

# When user clicks button
if st.button("Predict Quality"):
    # Create DataFrame for model
    input_data = pd.DataFrame({
        'Fluoride (mg/L)': [fluoride],
        'Turbidity (NTU)': [turbidity],
        'pH': [ph],
        'Temperature': [temperature]
    })

    # Make prediction
    prediction = model.predict(input_data)

    st.success(f"✅ Predicted Water Quality: {prediction[0]}")

