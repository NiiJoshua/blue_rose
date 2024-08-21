import streamlit as st
import pandas as pd
# import joblib
import pickle


# Load the trained model (assuming you've saved it)
# model = joblib.load("model_pkl")
with open("model.pkl", "rb") as f:
    model = pickle.load(f)


st.title("House Price Prediction for Blue Rose Ltd")

# Collect user input
city = st.selectbox("City", ["lapaz", "east_legon", "buduburam", "dansoman", "teshie", "kasoa", "awoshie", "cantonments", "osu", "gomoa"])
land_size = st.number_input("Land Size (in acres)", min_value=0.1)
house_type = st.selectbox("House Type", ["2 bedrooms", "pent house", "condo", "2 storey", "3 bedrooms detached", "2 bedrooms semi-detached", "5 bedrooms", "4 storey", "2 bedrooms", "2 bedrooms detached"])
inflation_rate = st.number_input("Inflation Rate", value=28)
exchange_rate = st.number_input("Exchange Rate", value=15.6)
proximity_to_amenities = st.selectbox("Proximity to Amenities", ["yes", "no"])
age_of_property = st.number_input("Age of Property (in years)", min_value=0)
property_condition = st.selectbox("Property Condition", ["excellent", "good", "fair", "poor"])

# Add a submit button
if st.button("Submit"):
    # Make prediction
    input_data = pd.DataFrame({
        "city": [city],
        "land_size": [land_size],
        "house_type": [house_type],
        "inflation_rate": [inflation_rate],
        "exchange_rate": [exchange_rate],
        "proximity_to_amenities": [proximity_to_amenities],
        "age_of_property": [age_of_property],
        "property_condition": [property_condition]
    })

    prediction = model.predict(input_data)[0]
    st.write(f"Predicted House Price: ${prediction:,.2f}")

