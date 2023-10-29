import streamlit as st
from datetime import datetime
import os

now = datetime.now()

print ("starting at: ",now)

picture = st.camera_input("First, take a picture...")

if picture:
    print ("picture was taken")
    with open ('test.jpg','wb') as file:
          print ("file is open")
          file.write(picture.getvalue())
          file.close()
          picture.close()
          st.image ("test.jpg","last picture taken")
          print ("file is overwritten")
else:
        print ("no picture was taken")
        st.write("no picture taken")