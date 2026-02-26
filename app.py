import streamlit as st
from PIL import Image
st.title("mi primera app")
st.header("Esta es mi pagina de presentación")

image = Image.open("matildaRelajada.jpeg")
st.image(image, caption:"matildaRelajada.jpeg")

texto=st.text_input("ingresa texto", "texto inicial")
st.write("el texto que haz escrito es",texto)
