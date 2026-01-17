import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("diabetes_model.pkl", "rb"))

# Streamlit page config
st.set_page_config(page_title="Diabetes Prediction", layout="centered")

# Custom CSS for colorful UI
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #d6eaff, #ffffff);
        }
        .title {
            font-size: 42px;
            color: #003566;
            font-weight: 700;
            text-align: center;
        }
        .subtitle {
            font-size: 18px;
            color: #444444;
            text-align: center;
            margin-bottom: 30px;
        }
        .stNumberInput > div > input {
            border-radius: 10px;
        }
        .predict-btn {
            background-color: #0077b6;
            color: #ffffff;
            padding: 12px 30px;
            border-radius: 10px;
            font-size: 18px;
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">🩺 Diabetes Prediction System</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Enter patient details to predict diabetes</p>', unsafe_allow_html=True)

# Input fields in two columns
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Pregnancies", 0, 20, 1)
    bp = st.number_input("Blood Pressure", 0, 140, 70)
    insulin = st.number_input("Insulin Level", 0, 900, 80)
    dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)

with col2:
    glucose = st.number_input("Glucose Level", 0, 200, 120)
    skin = st.number_input("Skin Thickness", 0, 100, 20)
    bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
    age = st.number_input("Age", 1, 120, 30)

# Predict button
if st.button("Predict", help="Click to see prediction"):
    input_data = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ High Risk: The person is likely DIABETIC.", icon="🚨")
    else:
        st.success("✅ Low Risk: The person is NOT diabetic.", icon="💚")
