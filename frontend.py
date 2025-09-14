import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict" 

st.title("Insurance Premium Category Predictor")
st.markdown("Enter your details below:")

# Input fields
age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)
smoker = st.selectbox("Are you a smoker?", options=[True, False])
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox(
    "Occupation",
    ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job']
)

if st.button("Predict Premium Category"):
    # --- Preprocessing here ---
    bmi = weight / (height ** 2)

    if age < 18:
        age_group = "child"
    elif age < 40:
        age_group = "young_adult"
    else:
        age_group = "adult"

    lifestyle_risk = "high" if smoker else "low"
    city_tier = "tier1" if city.lower() in ["mumbai", "delhi", "bangalore"] else "tier2"

    # Now build input_data in backend's expected format
    input_data = {
    "age": age,  # <-- add this
    "bmi": bmi,
    "age_group": age_group,
    "lifestyle_risk": lifestyle_risk,
    "city_tier": city_tier,
    "income_lpa": income_lpa,
    "occupation": occupation
        }


    try:
        response = requests.post(API_URL, json=input_data)
        result = response.json()

        if response.status_code == 200 and "response" in result:
            prediction = result["response"]
            st.success(f"Predicted Insurance Premium Category: **{prediction['predicted_category']}**")
            st.write("Confidence:", prediction["confidence"])
            st.write("Class Probabilities:")
            st.json(prediction["class_probabilities"])

        else:
            st.error(f"API Error: {response.status_code}")
            st.write(result)

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the FastAPI server. Make sure it's running.")
