# Load libraries
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly

# Load model
model = joblib.load("Model\\model.pkl")

# Define functions
def load_data(path):
    dataset = pd.read_csv(path)
    return dataset

# Load the dataset
data_path = "Dataset\\train_data.csv"
load_df = load_data(data_path)
test_df = pd.read_csv("Dataset\\test.csv")


#Define section
data = st.container()

#Adding visual of model prediction
st.write("Lihat prediksi model")
if st.button("Model's graph"):
    # we predict with the model
    result = model.predict(test_df)
    
    # Create a Plotly line chart for the model's predictions 
    fig = px.line(x=test_df.index, y=result, title="Model's Forecast")
    
    # Display the chart using st.plotly_chart() 
    st.subheader("Plot perkiraan model") 
    st.plotly_chart (fig)