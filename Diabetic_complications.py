import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open("random_forest_model.pkl", "rb"))

st.title("Diabetes Complications Prediction App")

st.write("Enter patient information to predict the risk of complications.")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120, value=40)
sex = st.selectbox("Sex", ["Male", "Female"])
duration = st.number_input("Duration of Diabetes (years)", min_value=0, max_value=50, value=5)
hba1c = st.number_input("HbA1c", min_value=3.0, max_value=20.0, value=7.0)
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
bp_systolic = st.number_input("Systolic BP", min_value=50, max_value=250, value=120)
bp_diastolic = st.number_input("Diastolic BP", min_value=30, max_value=150, value=80)
comorbidity = st.selectbox("Comorbidity", ["None", "Hypertension", "Dyslipidemia"])

# Prepare input data
input_data = pd.DataFrame({
    "Age": [age],
    "Sex": [sex],
    "Duration_years": [duration],
    "HbA1c": [hba1c],
    "BMI": [bmi],
    "BP_Systolic": [bp_systolic],
    "BP_Diastolic": [bp_diastolic],
    "Comorbidity": [comorbidity]
})

# One-hot encode categorical features
input_data = pd.get_dummies(input_data)

# Align columns with training data
expected_features = model.feature_names_in_
for col in expected_features:
    if col not in input_data.columns:
        input_data[col] = 0

# Reorder columns
input_data = input_data[expected_features]

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]  # probability of complication
    prob_percent = int(probability * 100)

    st.write(f"### Prediction Probability: {prob_percent}%")

    # Show progress bar
    st.progress(probability)

    # Risk message
    if prediction == 1:
        st.error("⚠️ High risk of complications detected.")
    else:
        st.success("✅ Low risk of complications detected.")

