import streamlit as st
import tensorflow as tf

model = tf.keras.models.load_model('model')

st.title('Sentiment Analysis')
txt_area = st.text_area('Enter Your Text')

review = [txt_area]
pred = model.predict(review)
pred.squeeze()

if pred.squeeze() > 0.5:
    st.text(pred.squeeze())
    st.success('Review Positif')
else:
    st.text(pred.squeeze())
    st.error('Review Negative')
