import streamlit as st
import joblib 


def load_model():
    with open('text_classification.pkl', 'rb') as file:
        load_model = joblib.load(file)
    return load_model

load_model = load_model()

#load_model_file_path = os.path.abspath('text_classification.pkl')

#load_model = joblib.load(load_model_file_path)


st.title('Text Classification')
st.write('''Enter your text to classify it is positive or negative''')


text = st.text_input("Enter your text")


text_predicted = load_model.predict([text])


ok = st.button('Classify text if it is Positive or Negative')
if ok:
    if text_predicted == ['pos']:

        st.subheader('The text is Positive')

    else: 
        st.subheader('The text is Negaive')




   



