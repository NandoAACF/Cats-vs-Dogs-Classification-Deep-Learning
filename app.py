import streamlit as st
import tensorflow as tf
from page_predict import show_predict
from page_evaluation import show_evaluation

page = st.sidebar.selectbox("Choose Option", ("Predict", "Model Evaluation"))

if page == 'Predict':
    show_predict()
elif page == 'Model Evaluation':
    show_evaluation()
