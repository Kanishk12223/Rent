import base64
import pandas as pd
import numpy as np
import streamlit as st
import pickle

pickle_in = open("rent.pk1", "rb")
rf = pickle.load(pickle_in)

def predict_price(bathrooms, bedrooms, longitude, latitude):
    prediction = rf.predict([[bathrooms, bedrooms, longitude, latitude]])
    return int(prediction)
def main():
    st.title("Apartment Price Prediction")
    with open('img.jpg', "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
    longitude = st.slider("Longitude", min_value= -74.10, max_value= -73.67, step= 0.01)
    latitude = st.slider("Latitude", min_value= 40.55, max_value= 40.94, step= 0.01)
    bathrooms = st.text_input("Number of Bathrooms", "Please type here")
    bedrooms = st.text_input("Number of Bedrooms", "Please type here")
    result = ""
    if st.button("Predict"):
        result= predict_price(bathrooms, bedrooms, longitude, latitude)
    st.success('The price for this apartment would be $ {}'.format(result))
if __name__ == '__main__':
    main()