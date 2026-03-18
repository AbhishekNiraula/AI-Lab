import numpy as np
import pandas as pd
import streamlit as st
from model import XORPerceptron

st.title("XOR Logic Implementation Using Multi-Layer Perceptron")
st.markdown("---")

x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])

df = pd.DataFrame(x, columns = ['Input 1', 'Input 2'])
df['Output'] = y
st.header("DATASET")
st.table(df)

st.sidebar.header("Training HyperParameters")
learning_rate = st.sidebar.slider("Learning Rate", 0.01, 1.0, 0.1)
epoch = st.sidebar.slider("Epoch", 1, 5000, 1000)

if "model" not in st.session_state:
    st.session_state.model = None

if st.button("Train Model"):
    model = XORPerceptron(lr = learning_rate, epoch = epoch)
    model.fit(x, y)
    st.session_state.model = model
    st.success("Model Trained Successfully")
    
if st.session_state.model is not None:
    model = st.session_state.model
    st.header("Final Parameters")
    st.write(f"Perceptron OR - Weights: {model.perceptron_or.weight}, Bias: {model.perceptron_or.bias}")
    st.write(f"Perceptron NAND - Weights: {model.perceptron_nand.weight}, Bias: {model.perceptron_nand.bias}")
    st.write(f"Perceptron AND - Weights: {model.perceptron_and.weight}, Bias: {model.perceptron_and.bias}")
    st.header("Predictions")
    predictions = model.predict(x)
    result = pd.DataFrame(x, columns=["Input 1", "Input 2"])
    result['Predicted'] = predictions
    
    st.table(result)
    st.header("Test Your Predictions")
    col1, col2 = st.columns(2)
    
    with col1:
        input1 = st.selectbox("Select First Input", [0, 1], key = "input1")
    
    with col2:
        input2 = st.selectbox("Select Second Input", [0, 1], key = "input2")
        
    pred = model.predict([[input1, input2]])
    st.info(f"The predicted value is {pred[0]}")