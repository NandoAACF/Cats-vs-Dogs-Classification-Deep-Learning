import streamlit as st

def show_evaluation():
    st.title('Model Evaluation')

    st.write('**Berikut adalah 3 model yang saya coba:**')
    st.write('1. CNN')
    st.write('2. VGG')
    st.write('3. InceptionV3 (Best Accuracy 99%))')

    st.subheader('CNN Accuracy & Loss')
    st.image('model_evaluation/cnn.png')
    st.write('Tampak bahwa akurasi CNN untuk data validation mencapai 91% pada epoch ke-12')

    st.subheader('VGG Accuracy & Loss')
    st.image('model_evaluation/vgg.png')
    st.write('Tampak bahwa akurasi VGG untuk data validation mencapai 93% pada epoch ke-6')
    st.write('Loss nya pun masih lebih baik daripada CNN')

    st.subheader('InceptionV3 Accuracy & Loss')
    st.image('model_evaluation/inception.png')
    st.write('Model InceptionV3 mendapatkan akurasi yang sangat tinggi.')
    st.write('Akurasi data validation mencapai 99% pada epoch ke-5 dan loss nya pun sangat kecil')

    st.subheader('Accuracy Comparison of that 3 Models')
    st.image('model_evaluation/comparison.png')
    st.write('Tampak bahwa model InceptionV3 menghasilkan akurasi tertinggi dibandingkan model lainnya')
    st.write('Akurasi CNN dan VGG tidak terlalu berbeda jauh, namun VGG lebih baik daripada CNN')
    st.write('Maka, model yang akan digunakan adalah InceptionV3.')
