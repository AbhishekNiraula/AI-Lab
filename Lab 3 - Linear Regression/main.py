# Importing necessary libraries
import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from model import LinearRegression
import streamlit as st

# Streamlit Title
st.title("Salary Prediction using Linear Regression!!")
data = pd.read_csv("Book1.csv")

# Preview Dataset
st.header("Dataset Preview")
st.dataframe(data)
# Convert into numpy array.
x= data["YearsExperience"].values.reshape(-1,1)
y = data["Salary"].values

# Train Test Split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(x_train,y_train)

# Make new prediction
y_pred = model.predict(x_test)

# Calculate the Error
mse = np.mean((y_test-y_pred)**2)
st.write(f"Mean square error: {mse}")
# Test Prediction
y_prediction = model.predict(5)
print(f"The prediction for given year is: {y_prediction}")

# Predictions for Visual Presentation
y_line = model.predict(x)
st.subheader("Regression line and datapoints")

plt.figure(figsize = (8,6))
plt.scatter(x_train,y_train,color="blue",s=20,label="TRAINING DATA")
plt.scatter(x_test,y_test,color="green",s=20,label= "TEST DATA")
plt.plot(x,y_line,color="red",linewidth=2, label="REGRESSION LINE")
plt.xlabel("YEAR EXPERIENCE")
plt.ylabel("SALARY")
st.pyplot(plt)

st.subheader("Predict Salary")
year = st.number_input("Enter experience", min_value=0.0,max_value=50.0,step=0.5)

predicted_salary = model.predict(np.array([[year]]))[0]
st.success(f"Predicted Salary{predicted_salary}")