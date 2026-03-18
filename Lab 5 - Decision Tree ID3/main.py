import numpy as np
import pandas as pd
import streamlit as st
from model import DecisionTreeID3
from graphviz import Digraph

def dict_to_graphviz(tree):
    dot = Digraph()
    counter = {"count": 0}
    
    def add_nodes_edges(tree, parent = None, edge_label = None):
        node_id = str(counter["count"])
        counter["count"] += 1
        
        if not isinstance(tree, dict):
            dot.node(node_id, label=str(tree), shape="box")
            if parent is not None:
                dot.edge(parent, node_id, label=edge_label)
            return
        
        root = next(iter(tree))
        dot.node(node_id, label=root)
        
        if parent is not None:
            dot.edge(parent, node_id, label=edge_label)
        
        for value, subtree in tree[root].items():
            add_nodes_edges(subtree,  parent=node_id, edge_label=str(value))
    
    add_nodes_edges(tree)
    return dot
        

st.set_page_config(page_title="Decision Tree ID3")

st.title("Decision Tree ID3 Implementation")

@st.cache_data
def load_data():
    return pd.read_csv("Purchase.csv")

data = load_data()

st.subheader("Dataset")
st.dataframe(data)

x = data.drop(columns = ["Purchase"])
y = data["Purchase"]

@st.cache_resource
def train_model(x, y):
    model = DecisionTreeID3()
    model.fit(x, y)
    return model

model = train_model(x, y)

st.subheader("Decision Tree Graph")
tree = dict_to_graphviz(model.tree)
st.graphviz_chart(tree)

st.divider()

st.subheader("Make a prediction")

holiday = st.selectbox("Holiday", options = data["Holiday"].unique())
discount = st.selectbox("Discount", options = data["Discount"].unique())
free_delivery = st.selectbox("Free Delivery", options = data["Free Delivery"].unique())

if st.button("Predict"):
    input_data = pd.DataFrame({
		"Holiday": [holiday],
		"Discount": [discount],
		"Free Delivery": [free_delivery],
	})
    output = model.predict(input_data)
    if output[0] == 'Yes':
        st.info("Item Purchased")
    else:
        st.warning("Item Unsold.")