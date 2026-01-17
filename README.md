# 🩺 Diabetes Prediction System – Frontend 🤖📊

<p align="center">
  <img src="https://img.icons8.com/color/96/heart-health.png"/>
  <img src="https://img.icons8.com/color/96/artificial-intelligence.png"/>
  <img src="https://img.icons8.com/color/96/python.png"/>
</p>

<p align="center">
  <b>A Machine Learning based Diabetes Prediction system with a colorful Streamlit frontend</b>
</p>

---

## 🚀 Project Overview

This project is a **Diabetes Prediction System** that uses **Machine Learning (Logistic Regression)** to predict whether a person is diabetic or not based on medical parameters.

The trained model is deployed using a **Streamlit frontend**, allowing users to enter patient details and receive instant predictions through a web interface.

---

## 🎯 Problem Statement

Diabetes is a serious health condition that requires early detection.

Manual diagnosis based only on symptoms may be inaccurate.  
👉 **Machine Learning helps analyze medical data and predict diabetes more reliably.**

---

## 📂 Dataset Information

- Dataset: **PIMA Indians Diabetes Dataset**
- File: `diabetes.csv`

### 📄 Features Used
- 🤰 Pregnancies  
- 🍬 Glucose  
- 🩸 Blood Pressure  
- 📏 Skin Thickness  
- 💉 Insulin  
- ⚖️ BMI  
- 🧬 Diabetes Pedigree Function  
- 🎂 Age  

🎯 Target:
- `0` → Not Diabetic  
- `1` → Diabetic  

---

## 🧠 Machine Learning Model

- 🔹 Algorithm: **Logistic Regression**
- 🔹 Problem Type: **Binary Classification**
- 🔹 Language: **Python**

---

## 🛠️ Technologies Used

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white"/>
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
</p>

---

## 🔄 Project Workflow

1️⃣ Load dataset from CSV  
2️⃣ Preprocess medical data  
3️⃣ Train Logistic Regression model  
4️⃣ Save trained model (`.pkl`)  
5️⃣ Build Streamlit frontend  
6️⃣ Take user input  
7️⃣ Predict diabetes result  

---

▶️ How to Run the Project
1️⃣ Install dependencies
pip install streamlit pandas numpy scikit-learn

2️⃣ Train the model
python diabetes_model.py

3️⃣ Run the frontend
streamlit run app.py


🌐 Open in browser:

http://localhost:8501

📈 Model Output

✅ Not Diabetic → Green success message

⚠️ Diabetic → Red warning message

The result is displayed instantly on the frontend.

🎓 Learning Outcomes

Understanding medical datasets

Logistic Regression implementation

CSV-based data handling

Model deployment using Streamlit

Frontend + ML integration

📌 Use Cases

🎓 Academic Mini / Major Project
💼 Machine Learning Portfolio
🩺 Healthcare Prediction System
🧠 ML Fundamentals Practice

👤 Author
<p align="center"> <img src="https://avatars.githubusercontent.com/Nandan0402" width="120" style="border-radius:50%;" /> </p> <p align="center"> <b>Nandan B</b><br> BCA Student | Machine Learning Enthusiast </p> <p align="center"> 🌐 <a href="https://github.com/Nandan0402">GitHub</a> | 💼 <a href="https://www.linkedin.com/in/nandan-b-2a9b1b334/">LinkedIn</a> </p>
⭐ Conclusion

This project demonstrates how Machine Learning models can be deployed as real-world applications using Streamlit, making complex predictions accessible through a simple and interactive UI.

⭐ If you find this project useful, please star the repository.

## 📁 Project Structure

```text
diabetes-prediction-system-Frontend/
│
├── diabetes.csv
├── diabetes_model.py
├── diabetes_model.pkl
├── app.py
├── requirements.txt
└── README.md
