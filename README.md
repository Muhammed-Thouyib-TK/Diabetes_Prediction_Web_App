# 🩺 Diabetes Risk Prediction System (Logistic Regression + Streamlit)

An end-to-end machine learning pipeline to predict diabetes risk using patient medical data, deployed with Streamlit Community Cloud for interactive, real-time predictions.

---

## 🎯 Objective

Build a machine learning system that:

- Predicts whether a patient is diabetic or non-diabetic  
- Provides real-time predictions through a user-friendly Streamlit web application  

---

## 📊 Dataset & Preprocessing

**Dataset:** Pima Indians Diabetes Dataset

### Preprocessing Steps

- Replaced medically invalid zero values in critical features  
- Performed leakage-safe median imputation using training data only  
- Applied stratified train–test split to preserve class balance  
- Standardized features using StandardScaler  

---

## 🧪 Model Architecture

**Algorithm:** Logistic Regression (Binary Classification)

### Model Design

- Cross-validated Logistic Regression for optimal regularization  
- Balanced class weights to handle class imbalance  
- Sigmoid activation for probability-based predictions  
- Odds ratio–based feature interpretation for explainability  

---

## ⚙️ Deployment

- Model saved as `diabetes_model.pkl`  
- Streamlit application includes:
  - Patient data input form  
  - Automatic preprocessing and scaling  
  - Real-time prediction results  
  - Visual risk indicators  

Deployed using **Streamlit Community Cloud** for online accessibility.

---

## 🔍 Key Insights

- Glucose, BMI, age, and family history are the most influential features  
- Achieves stable ROC-AUC performance (~0.81)  
- Cross-validation ensures robust and unbiased predictions  

---

## 🔮 Future Scope

- Add non-linear feature interactions  
- Explore ensemble and deep learning models  
- Integrate explainable AI dashboards  

---

## 🛠 Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Streamlit  
- Matplotlib, Seaborn  

---

## 🚀 Live Demo

🔗 **Try the App** – https://diabetes-prediction-web-app-new.streamlit.app/
