import streamlit as st

from streamlit_back_camera_input import back_camera_input

image = back_camera_input()
if image:
    with open ('test.jpg','wb') as file:
          file.write(image.getvalue())
          file.close()
    st.image('test.jpg')