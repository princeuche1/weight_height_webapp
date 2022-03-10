import numpy as np
import pickle
import streamlit as st
import os
import json

path = os.path.dirname(os.path.abspath(__file__))

# read the pickle file with the model and store it in a variable
with open(f"{path}/height_model_pickle", "rb") as pickle_in:
    loaded_model = pickle.load(pickle_in)


def weight_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = np.reshape(input_data_as_numpy_array, (-1, input_data_as_numpy_array.size))
    # input_data_reshaped = input_data_as_numpy_array.reshape(-1, 1)
    prediction = loaded_model.predict([[input_data]])
    return prediction


def dict_map(variable):
    with open("dict.json", "r") as json_in:
        dictionary_list = json.load(json_in)
    for dictionary in dictionary_list:
        for key in dictionary:
            if key == variable:
                variable = dictionary[key]
                return variable


def main():
    """
    Constucts the streamlit web app
    """
    # give a title to the webapp
    st.title('Weight-Height Prediction Web App')
    # Get input from user
    height = st.text_input("Input height")

    # code for the prediction
    weight = ' '
    # creating a button for prediction
    if st.button("Predict"):
        st.success(weight_prediction(height))



if __name__ == "__main__":
    main()

# to run app: streamlit run streamlit-streamlit_code.py
