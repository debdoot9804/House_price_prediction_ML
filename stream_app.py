import streamlit as st
import pickle
import numpy as np

# Load the model and scaler
scaler = pickle.load(open("scaler.pkl", "rb"))
model = pickle.load(open("xgb_model.pkl", "rb"))

# Streamlit UI
st.title("House Price Prediction App")

# User Inputs
latitude = st.number_input("Latitude")
housing_median_age = st.number_input("Housing Median Age")
total_rooms = st.number_input("Total Rooms")
households = st.number_input("Households")
median_income = st.number_input("Median Income")
ocean_proximity_INLAND = st.selectbox("Ocean Proximity INLAND", [0, 1])
ocean_proximity_NEAR_BAY = st.selectbox("Ocean Proximity NEAR BAY", [0, 1])
ocean_proximity_NEAR_OCEAN = st.selectbox("Ocean Proximity NEAR OCEAN", [0, 1])

# Predict Button
if st.button("Predict"):
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
