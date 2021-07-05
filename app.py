import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from werkzeug.utils import secure_filename
st.set_option('deprecation.showfileUploaderEncoding', False)

html_temp = """
   <div class="" style="background-color:green;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Poornima Institute of Engineering & Technology</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">Digital Image Processing II - Midterm Examination</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)
  
st.title("""
        Collor Palette
         """
         )
file= st.file_uploader("Please upload image", type=("jpg", "png"))
R = st.slider('R', min_value=0, max_value=255, step=1)

import cv2
from  PIL import Image, ImageOps
def import_and_predict(image_data):
  img = np.zeros((255,255,255), np.uint8)
  image = image.img_to_array(img)
  img_reshap= np.expand_dims(image, axis=0)
  img_reshap = preprocess_input(img_reshap)
   
  image_data[:] = [R]
  st.image(image_data, use_column_width=True)
    
if st.button("Change Color"):
  result=import_and_predict(image)
  
if st.button("About"):
  st.header(" Ayush Jain")
  st.subheader("Student")
html_temp = """
   <div class="" style="background-color:orange;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:20px;color:white;margin-top:10px;">Digital Image processing Experiment</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)
