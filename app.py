import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load model
model = load_model("snake_classifier_model.keras")

st.title("Snake Classifier")

uploaded_file = st.file_uploader("Upload a snake image", type=["jpg","png"])
if uploaded_file is not None:
    img = image.load_img(uploaded_file, target_size=(48,48), color_mode="grayscale")
    x = image.img_to_array(img)/255.0
    x = np.expand_dims(x, axis=0)
    prediction = model.predict(x)
    classes = ["Non-Venomous", "Venomous"]
    st.write("Predicted class:", classes[np.argmax(prediction)])
