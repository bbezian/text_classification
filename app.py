import streamlit as st
import os
import joblib 
import numpy as np 
import pandas as pd


load_model_file_path = os.path.abspath('text_classification.pkl')

load_model = joblib.load(load_model_file_path)


st.title('Text Classification')
st.write('''Enter your text to classify it is positive or negative''')


text = st.text_input("Enter your text")


text_predicted = load_model.predict([text])

if text_predicted == ['pos']:

    st.title('The text is Positive')

else: 
    st.title('The text is Negaive')

   



