import tensorflow as tf
from google.colab import files, drive

# Step 1: Upload local model
uploaded = files.upload()   # choose snake_classifier_model.keras

# Step 2: Load the uploaded model
model = tf.keras.models.load_model("snake_classifier_model.keras")
print(" Model loaded successfully")

# Step 3: Save permanently to Google Drive
drive.mount('/content/drive')
!mkdir -p /content/drive/MyDrive/SNAKE_CLASSIFIER
!cp snake_classifier_model.keras /content/drive/MyDrive/SNAKE_CLASSIFIER/
print("Model copied to Google Drive: /content/drive/MyDrive/SNAKE_CLASSIFIER/")

import gradio as gr
import numpy as np
from tensorflow.keras.preprocessing import image

labels = ['Non-Venomous', 'Venomous']

def predict_snake(img):
    try:
        img = img.convert("RGB")  # make sure 3 channels
        img = img.resize((160, 160))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        preds = model.predict(img_array)
        class_idx = np.argmax(preds, axis=1)[0]
        confidence = preds[0][class_idx]

        return {labels[class_idx]: float(confidence)}

    except Exception as e:
        print("⚠️ Error inside predict_snake:", e)  # logs in Colab output
        raise e   # forces Gradio to display error trace


# Gradio app
iface = gr.Interface(
    fn=predict_snake,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=2),
    title="Salazar 🐍",
    description="Upload a snake image to classify whether it's Venomous or Non-Venomous."
)

iface.launch()
