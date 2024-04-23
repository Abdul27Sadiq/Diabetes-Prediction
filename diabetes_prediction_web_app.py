import numpy as np
import pickle
import streamlit as st

# Loading the saved Model
loaded_model = pickle.load(open(r'C:\Users\abdul\Downloads\Dibates_Prediction\core\code\trained_model_sav', 'rb'))

# Creating a function for Prediction

def diabetes_prediction(input_data):
    
    # Change the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    # Reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if(prediction[0]==0):
         return'The person is not Diabetic'
    else:
        return'The person is Diabetic'

def main():
    
    # Give a Title
    st.title('Diabetes Prediction Web App')
    
    # Getting the input from the user
    Pregnencies = st.text_input("No of Pregnencies")
    Glucose = st.text_input("Glucose level")
    BloodPressure = st.text_input("BloodPressure level")
    SkinThickness = st.text_input("SkinThickness value")
    Insulin = st.text_input("what is Insulin level")
    BMI = st.text_input("BMI rate")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value")
    Age = st.text_input("Age of the Person")
    
    # Code for Prediction
    diabetes = ''
    
    # Creating a button for Prediction
    if st.button('Diabetes Test Result'):
        
        diabetes = diabetes_prediction([Pregnencies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        #  # Convert all inputs to float
        # input_data = [float(Pregnencies), float(Glucose), float(BloodPressure), float(SkinThickness), float(Insulin), float(BMI), float(DiabetesPedigreeFunction),
        #               float(Age)]
        
        #   # Make prediction
        # diabetes = diabetes_prediction(input_data)
        
        st.success(diabetes)
      
if __name__ == '__main__':
         main()