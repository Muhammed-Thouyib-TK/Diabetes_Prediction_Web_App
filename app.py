import streamlit as st
import numpy as np
import pickle

st.set_page_config(page_title="Diabetes Prediction", layout="centered")

# Load trained model & scaler
model = pickle.load(open("diabetes_model.pkl","rb"))
scaler = pickle.load(open("scaler.pkl","rb"))

st.title("🩺 Diabetes Risk Prediction System")
st.markdown("Enter patient medical information below:")

col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=0)
    Glucose = st.number_input("Glucose Level", min_value=50, max_value=300, value=120)
    BloodPressure = st.number_input("Blood Pressure", min_value=40, max_value=200, value=70)
    SkinThickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)

with col2:
    Insulin = st.number_input("Insulin Level", min_value=0, max_value=900, value=80)
    BMI = st.number_input("BMI", min_value=10.0, max_value=70.0, value=25.0)
    DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
    Age = st.number_input("Age", min_value=1, max_value=120, value=30)

if st.button("Predict Diabetes"):
    user_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                            Insulin, BMI, DiabetesPedigreeFunction, Age]])
    user_scaled = scaler.transform(user_data)
    prediction = model.predict(user_scaled)

    if prediction[0] == 1:
        st.error("⚠ High Risk: Diabetes Detected")
    else:
        st.success("✅ No Diabetes Detected")
