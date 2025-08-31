# Salazar – Snake Classifier

Salazar is a minimalistic web app that classifies snake images as **Venomous** or **Non-Venomous** using a pre-trained deep learning model. The app is built with **Streamlit** and TensorFlow.

## Features

- Upload a snake image and get an instant prediction.
- Pre-trained model optimized for accurate classification.
- Simple, clean, and interactive user interface.

## Installation

1. Clone the repository:  
```bash
git clone https://github.com/yourusername/salazar-snake-classifier.git
cd salazar-snake-classifier

## Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

## Install dependencies:

pip install -r requirements.txt


## Usage

Run the app locally:
streamlit run app.py
Upload an image of a snake (jpg or png).
The app will display the predicted class: Venomous or Non-Venomous.

## Model

The model is trained on a curated snake dataset on kaggle- "Snake Dataset- India".
Saved as snake_classifier_model.keras.
Uses MobileNetV2 as the base model with transfer learning.
