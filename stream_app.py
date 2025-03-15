import streamlit as st
import pickle
import numpy as np

# Load the model and scaler
scaler = pickle.load(open("scaler.pkl", "rb"))
model = pickle.load(open("xgb_model.pkl", "rb"))

# Streamlit UI
st.title("House Price Prediction App")

# User Inputs
latitude = st.number_input("Latitude", format="%.6f")
housing_median_age = st.number_input("Housing Median Age", min_value=0)
total_rooms = st.number_input("Total Rooms", min_value=1)
households = st.number_input("Households", min_value=1)
median_income = st.number_input("Median Income", min_value=0.0, format="%.2f")
ocean_proximity_INLAND = st.selectbox("Ocean Proximity INLAND", [0, 1])
ocean_proximity_NEAR_BAY = st.selectbox("Ocean Proximity NEAR BAY", [0, 1])
ocean_proximity_NEAR_OCEAN = st.selectbox("Ocean Proximity NEAR OCEAN", [0, 1])

# Predict Button
if st.button("Predict"):
    # Check if any input is missing
    if latitude == 0.0 or median_income == 0.0:
        st.error("Error: Please enter valid values for all fields before predicting!")
    else:
        # Convert inputs into array
        features = np.array([[latitude, housing_median_age, total_rooms, households, 
                              median_income, ocean_proximity_INLAND, 
                              ocean_proximity_NEAR_BAY, ocean_proximity_NEAR_OCEAN]])
        
        # Scale the input
        data_scaled = scaler.transform(features)
        
        # Make Prediction
        prediction = model.predict(data_scaled)[0]
        
        # Show Prediction
        st.success(f"Predicted House Price: ${prediction:.2f}")
