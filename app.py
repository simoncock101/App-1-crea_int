import streamlit as st
from PIL import Image

st.title("HOLA !!! mi  nombre es Simon ")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open('Space.jpg')
st.image(image, caption='Interfaces multimodales')
