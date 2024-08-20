import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Load the trained model
model = RandomForestRegressor()
model.load('house_price_model.pkl')

# Define the Streamlit app
st.title("House Price Prediction")

# Input fields for property features
city = st.selectbox("City", ["lapaz", "east_legon", "buduburam", "dansoman", "teshie", "kasoa", "awoshie", "cantonments", "osu", "gomoa"])
land_size = st.number_input("Land Size (acres)", min_value=1.0, step=0.5)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, step=1)
inflation_rate = st.number_input("Inflation Rate (%)", min_value=0.0, step=0.1)
exchange_rate = st.number_input("Exchange Rate", min_value=0.0, step=0.1)
proximity_to_amenities = st.selectbox("Proximity to Amenities", ["Yes", "No"])
age_of_property = st.number_input("Age of Property (years)", min_value=1, step=1)
property_condition = st.selectbox("Property Condition", ["Excellent", "Good", "Fair", "Poor"])

# Predict button
if st.button("Predict Price"):
    # Preprocess the input data
    X_new = np.array([[city, land_size, bedrooms, inflation_rate, exchange_rate, proximity_to_amenities, age_of_property, property_condition]])
    
    # Make the prediction
    predicted_price = model.predict(X_new)
    
    # Display the predicted price
    st.write(f"Predicted Price: GHS {predicted_price[0]:.2f}")