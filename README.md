# diabetes-complications-prediction
Machine learning project for predicting diabetes complications using patient clinical data. Includes data preprocessing, model training, evaluation, and deployment with Streamlit.
# Diabetes Complications Prediction

## 📌 Project Overview
This project aims to **predict diabetes complications** based on patient clinical data using **Machine Learning models**.  
It demonstrates a full pipeline:
- Data preprocessing
- Exploratory Data Analysis (EDA)
- Model training and evaluation
- Deployment with **Streamlit app**

---

## 📊 Dataset
The dataset contains the following columns:
- `Age`
- `Sex`
- `Duration_years` (duration of diabetes in years)
- `HbA1c`
- `BMI`
- `BP_Systolic`
- `BP_Diastolic`
- `Comorbidity`
- `Complication` (Target variable: 0 = No complication, 1 = Complication)

---

## ⚙️ Workflow
1. **Data Preprocessing**
   - Handle missing values
   - One-hot encoding for categorical variables
   - Train-test split

2. **Model Training**
   - Logistic Regression
   - Random Forest Classifier
   - Evaluation with Accuracy, Precision, Recall, F1-score

3. **Deployment**
   - Built with **Streamlit**
   - Interactive form for users to enter patient data
   - Model predicts the risk of complications

---
Deployment

The app can be deployed on Streamlit Community Cloud.

(https://diabetic-complications-predict.streamlit.app/)

📌 Example

Input your medical details in the web form → Click "Predict" → Get instant prediction (Diabetic Complications: Yes / No) and probability.
