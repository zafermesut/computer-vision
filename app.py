import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Image Upload with Brightness and Contrast Adjustments")

uploaded_file = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png"])
picture = st.camera_input("Take a picture", )

brightness = st.slider("Brightness", min_value=-100, max_value=100, value=0)
contrast = st.slider("Contrast", min_value=0.5, max_value=3.0, value=1.0, step=0.1)


if picture is not None:
    image = Image.open(picture)
    img_np = np.array(image) 
   
    if img_np.shape[-1] == 4:
        img_np = img_np[:, :, :3]

    img_adjusted = cv2.convertScaleAbs(img_np, alpha=contrast, beta=brightness)

    st.image(img_adjusted, caption="Adjusted Image", use_column_width=True)
    st.image(image, caption="Original Image", use_column_width=True)


if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_np = np.array(image) 
    
    if img_np.shape[-1] == 4:
        img_np = img_np[:, :, :3]
    
    img_adjusted = cv2.convertScaleAbs(img_np, alpha=contrast, beta=brightness)
    
    st.image(img_adjusted, caption="Adjusted Image", use_column_width=True)
    st.image(image, caption="Original Image", use_column_width=True)
