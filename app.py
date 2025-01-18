
import pickle
import streamlit as st
import pandas as pd
import numpy as np

# Load the model
rfr = pickle.load(open('calories.pkl', 'rb'))
st.title('Calories Burn Prediction')

# Define gender options
GenderOption = ['Male', 'Female']

# Prediction function
def pred(Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp):
    Features = np.array([[Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp]])
    Prediction = rfr.predict(Features)  # Removed reshape
    return Prediction[0]  # Return the first element directly

# User inputs
UserGender = st.selectbox('Select Gender', GenderOption, help="Choose your gender")
Age = st.text_input('Age', placeholder="Enter your age")
Height = st.text_input('Height', placeholder='Enter Height in cm')
Weight = st.text_input('Weight', placeholder='Enter Weight in kg')
Duration = st.text_input('Duration', placeholder='Enter Duration in min')
Heart_Rate = st.text_input('Heart Rate', placeholder='Enter Heart Rate in bpm')
Body_Temp = st.text_input('Body Temperature', placeholder='Enter Body Temperature in Celsius')

# Gender encoding: Male = 0, Female = 1
Gender = 0 if UserGender == 'Male' else 1

if st.button('Predict'):
    try:
        # Convert inputs to numeric
        Age = int(Age)
        Height = float(Height)
        Weight = float(Weight)
        Duration = float(Duration)
        Heart_Rate = float(Heart_Rate)
        Body_Temp = float(Body_Temp)

        # Validate and clip inputs
        Age = max(20, min(Age, 80))
        Height = max(123, min(Height, 222))
        Weight = max(36, min(Weight, 136))
        Duration = max(1, min(Duration, 30))
        Heart_Rate = max(67, min(Heart_Rate, 128))
        Body_Temp = max(37, min(Body_Temp, 41))

        # Perform prediction
        result = pred(Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp)
        st.write(f"You have burnt approximately {result:.2f}  Calories.")
    except ValueError:
        st.error("Please enter valid numeric values for all fields.")
