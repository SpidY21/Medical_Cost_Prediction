import pickle
import streamlit as st
import numpy as np
from lightgbm import LGBMRegressor
# import joblib
# import requests

# model_url = "https://github.com/SpidY21/Medical_Cost_Prediction/blob/master/model.pickle"
# response = requests.get(model_url)
# with open("model.pkl", "wb") as f:
#     f.write(response.content)
#
# model = joblib.load("model.pkl")

# model = pickle.load((open("https://github.com/SpidY21/Medical_Cost_Prediction/blob/master/model.pickle", 'rb')))

model = pickle.load((open("model.pickle", 'rb')))


def predictor(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = model.predict(input_data_reshaped)
    return prediction


def main():
    st.title('Medical Insurance Calculator...')
    age = st.number_input("Enter your age:- ", value=None, placeholder="Enter you age...")
    sex = st.selectbox("Enter your sex:- ", ["Male", "Female"])
    sex_num = 1  # For Male
    if sex == 'Female':
        sex_num = 0
    bmi = st.number_input("Enter your Body Mass Index(BMI):- ", value=None, placeholder="Enter you BMI...")
    child = st.selectbox("Enter how many children do you have:- ", [0, 1, 2, 3, 4, 5])
    smoker = st.selectbox("Are you a Smoker or not:- ", ["Yes", "No"])
    smoker_num = 1  # for Smoker Yes
    if smoker == "No":
        smoker_num = 0
    region = st.selectbox("Enter you region:- ", ["Northeast", "Northwest", "Southwest", "Southeast"])
    region_num = 0  # For Northeast
    if region == "Northwest":
        region_num = 1
    elif region == "Southwest":
        region_num = 3
    elif region == "Southeast":
        region_num = 2
    else:
        region_num = 0

    input_variables = [age, sex_num, bmi, child, smoker_num, region_num]

    if st.button("Predict"):
        st.write(f"The cost of you insurance will be {round(predictor(input_variables)[0], 3)} $")


if __name__ == '__main__':
    main()
