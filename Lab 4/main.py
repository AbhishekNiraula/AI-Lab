# Importing necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
from model import LogisticRegression

# Reading the data
st.title("Logistic Regression")

data = pd.read_csv("Social_Network_Ads.csv")

# Removing the initial data titles.
data = data.iloc[:, 1: ]

# Get the actual values.
x = data[["Age", "EstimatedSalary"]].values
y = data["Purchased"].values

# Scaling the features to have mean=0 and standard deviation=1.
# This is necessary because features have different scales (AGE: 20-80, IQ: 10000-150000).
# Scaling ensures faster convergence in gradient descent and prevents features with larger values from dominating.
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Dataset Preview")
    st.dataframe(data)

with col2:
    st.subheader("Data Visualization")
    fig, ax = plt.subplots()
    
    scatter = ax.scatter(x[:, 0], x[:, 1], c = y)
    ax.set_xlabel("Age")
    ax.set_ylabel("EstimatedSalary")
    
    st.pyplot(fig)

st.sidebar.header("Model Hyperparameter")
lr = st.sidebar.slider("Learning Rate", 0.001, 1.0, 0.1)

n_iters = st.sidebar.slider("Number of Iterations", 1000, 5000, 2000)

# If button pressed, then begin the model fitting.
if st.button("Train Model"):
    x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.3, random_state=42) 
    model = LogisticRegression(lr, n_iters)
    model.fit(x_train, y_train)
    
    y_pred = model.prob(x_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    
    st.session_state["model"] = model
    st.session_state["scaler"] = scaler
    st.session_state["accuracy"] = accuracy
    st.session_state["cm"] = cm
    # st.session_state["loss"] = model.loss_history
    st.session_state["trained"] = True

if "trained" in st.session_state:
    st.subheader("Model Performance")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Accuracy", f"{st.session_state['accuracy']:.4f}")
    
    with col2:
        st.write("**Confusion Matrix:**")
        st.dataframe(pd.DataFrame(st.session_state['cm'], 
                                   columns=['Predicted 0', 'Predicted 1'],
                                   index=['Actual 0', 'Actual 1']))
    
    st.subheader("Training Loss Curve")
    fig, ax = plt.subplots()
    ax.plot(st.session_state["model"].loss_history)
    ax.set_xlabel("Iterations")
    ax.set_ylabel("Loss")
    ax.set_title("LOSS VS ITERATIONS")
    st.pyplot(fig)

st.subheader("Predict")
age_input = st.number_input("Enter Age", 18, 65, 30)
salary_input = st.number_input("Enter Estimated Salary", 15000, 150000, 50000)

if st.button("Predict Purchase"):
    if "model" not in st.session_state:
        st.error("You have not trained your model")
    else:
        model = st.session_state["model"]
        scaler = st.session_state["scaler"]
        value = np.array([[age_input, salary_input]])
        value_scaled = scaler.transform(value)
        
        probability = model.predict(value_scaled[0])
        prob_value = probability.item() if isinstance(probability, np.ndarray) else probability
        
        pred = model.prob(value_scaled[0])
        pred_value = pred.item() if isinstance(pred, np.ndarray) else pred
        
        # Display probability
        st.info(f"**Purchase Probability: {prob_value*100:.2f}%**")
        
        if pred_value == 1:
            st.success("User will purchase")
        else:
            st.warning("User will not purchase")
            