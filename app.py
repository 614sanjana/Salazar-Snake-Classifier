import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Load the model
model = tf.keras.models.load_model("snake_classifier_model.keras")

# Class labels
classes = ["Non-Venomous", "Venomous"]

st.title("Snake Classifier")

# Upload image
uploaded_file = st.file_uploader("Upload a snake image", type=["jpg", "png"])
if uploaded_file is not None:
    # Load image with the correct size and channels
    img = image.load_img(uploaded_file, target_size=(160, 160))  # 160x160 RGB
    x = image.img_to_array(img)
    x = (x / 127.5) - 1  # normalize as in training
    x = np.expand_dims(x, axis=0)  # add batch dimension

    # Predict
    prediction = model.predict(x)
    
    # Since your model uses BinaryCrossentropy from logits
    pred_class = int(tf.sigmoid(prediction) > 0.5)
    
    st.write("Predicted class:", classes[pred_class])
