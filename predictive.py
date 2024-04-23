import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn import svm

# Loading the saved Model
loaded_model = pickle.load(open('C:\Users\abdul\Downloads\Dibates_Prediction\core\code\trained_model_sav', 'rb'))

input_data = (4,110,92,0,0,37.6,0.191,30)

# Change the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# Reshape the numpy array as we are predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction=loaded_model.predict(input_data_reshaped)
print(prediction)

if(prediction[0]==0):
  print('The person is not Diabetic')
else:
  print('The person is Diabetic')