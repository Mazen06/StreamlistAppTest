import streamlit as st
import numpy as np
import datetime
from PIL import Image


d = st.date_input("When's your birthday", datetime.date(2023, 12, 5))
st.write('Your birthday is:', d)



values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)



picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)


color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)


title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)


txt = st.text_area(
    "Text to analyze","",
    )

st.write(f'You wrote {len(txt)} characters.')


tab1, tab2 = st.tabs(["About", "Contact"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")

# You can also use "with" notation:
with tab1:
    st.radio('Select one:', [1, 2])