# import streamlit as st
# import pandas as pd
# import numpy as np
# import pickle
#
# # Load Model
# rfr = pickle.load(open('rfr.pkl','rb'))
# x_train = pd.read_csv('x_train.csv')
#
# def pred(Gender, Age,Height,Weight,Duration,Heart_Rate,Body_Temp):
#     features = np.array([[Gender, Age,Height,Weight,Duration,Heart_Rate,Body_Temp]])
#     predictions = rfr.predict(features).reshape(1, -1)
#     return predictions[0]
#
#
# # Web
# st.title("Calories Burn Prediction")
# Gender = st.selectbox('Gender',x_train['Gender'])
# Age = st.selectbox('Age',x_train['Age'])
# Height = st.selectbox('Height',x_train['Height'])
# Weight = st.selectbox('Weight',x_train['Weight'])
# Duration = st.selectbox('Duration (minute)',x_train['Duration'])
# Heart_Rate = st.selectbox('Heart Rate (bpm)',x_train['Heart_Rate'])
# Body_Temp = st.selectbox('Body Temperature',x_train['Body_Temp'])
#
#
# result = pred(Gender, Age,Height,Weight,Duration,Heart_Rate,Body_Temp)
#
# if st.button('predict'):
#     if result:
#         st.write("You have consumed this Calories: ", result)
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load Model
rfr = pickle.load(open('rfr.pkl','rb'))
x_train = pd.read_csv('x_train.csv')

# Predict Function
def pred(Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp):
    features = np.array([[Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp]])
    predictions = rfr.predict(features).reshape(1, -1)
    return predictions[0]

# 🎨 Stylish CSS
st.markdown("""
    <style>
    html, body {
        background-color: #eaf6ff;
    }
    .main-container {
        background: linear-gradient(to right, #fceabb, #f8b500);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    }
    .stButton > button {
        background-color: #ff6f61;
        color: white;
        border-radius: 10px;
        border: none;
        font-size: 16px;
        padding: 10px 30px;
        margin-top: 20px;
    }
    .stButton > button:hover {
        background-color: #e75b50;
    }
    .stSelectbox label {
        font-weight: bold;
        color: #1e3d59;
    }
    .stTitle {
        color: #1e3d59;
        font-family: 'Segoe UI', sans-serif;
    }
    .prediction-box {
        background-color: #d1f7c4;
        padding: 20px;
        border-radius: 10px;
        color: #155724;
        font-weight: bold;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# 🎯 App Layout
st.markdown("<div class='main-container'>", unsafe_allow_html=True)
st.title("🔥 Calories Burn Prediction")

# Gender Mapping for UI
gender_mapping = {
    0: "0 - Male",
    1: "1 - Female"
}
# Reverse map for prediction
gender_reverse = {v: k for k, v in gender_mapping.items()}

# Show gender options as 0 - Male, 1 - Female
gender_display = st.selectbox("👤 Select Gender", list(gender_mapping.values()))
Gender = gender_reverse[gender_display]  # Get original 0 or 1

# Other Inputs
Age = st.selectbox('🎂 Select Age', sorted(x_train['Age'].unique()))
Height = st.selectbox('📏 Select Height (cm)', sorted(x_train['Height'].unique()))
Weight = st.selectbox('⚖️ Select Weight (kg)', sorted(x_train['Weight'].unique()))
Duration = st.selectbox('⏱️ Duration (minutes)', sorted(x_train['Duration'].unique()))
Heart_Rate = st.selectbox('❤️ Heart Rate (bpm)', sorted(x_train['Heart_Rate'].unique()))
Body_Temp = st.selectbox('🌡️ Body Temperature (°C)', sorted(x_train['Body_Temp'].unique()))

# Predict
if st.button('💪 Predict Calories Burned'):
    result = pred(Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp)
    st.markdown(f"<div class='prediction-box'>🔥 You Burned <b>{result[0]:.2f}</b> calories.</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


