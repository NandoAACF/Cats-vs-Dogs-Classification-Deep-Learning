import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps

@st.cache_resource()
def load_model():
    model = tf.keras.models.load_model('inceptionV3.h5')
    return model

data = load_model()

def show_predict():
    st.title('Cat vs Dog Classification')
    file = st.file_uploader('Please upload a cat/dog image file', type=['jpg', 'png'])

    if file is None:
        st.text('')
    else:
        image = Image.open(file)
        st.image(image, use_column_width=True)
        image = np.asarray(image)
        image = tf.image.resize(image, [224, 224])
        image = np.expand_dims(image, axis=0)
        image = image/255.0

        predict = data.predict(image)
        score = np.max(predict)
        predict = np.argmax(predict)

        if predict == 0:
            st.subheader('This is a cat with {:.2f}% confidence'.format(score*100))
        elif predict == 1:
            st.subheader('This is a dog with {:.2f}% confidence'.format(score*100))

