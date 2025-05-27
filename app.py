import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# Set page configuration first
st.set_page_config(page_title="Traffic Sign Classifier", layout="centered")

# Load the model and class names
@st.cache_resource
def load_model_and_classes():
    model = load_model('traffic_classifier_model.h5')
    classes = {
        1: 'Speed limit (20km/h)', 2: 'Speed limit (30km/h)', 3: 'Speed limit (50km/h)', 4: 'Speed limit (60km/h)',
        5: 'Speed limit (70km/h)', 6: 'Speed limit (80km/h)', 7: 'End of speed limit (80km/h)', 8: 'Speed limit (100km/h)',
        9: 'Speed limit (120km/h)', 10: 'No passing', 11: 'No passing veh over 3.5 tons', 12: 'Right-of-way at intersection',
        13: 'Priority road', 14: 'Yield', 15: 'Stop', 16: 'No vehicles', 17: 'Veh > 3.5 tons prohibited', 18: 'No entry',
        19: 'General caution', 20: 'Dangerous curve left', 21: 'Dangerous curve right', 22: 'Double curve', 23: 'Bumpy road',
        24: 'Slippery road', 25: 'Road narrows on the right', 26: 'Road work', 27: 'Traffic signals', 28: 'Pedestrians',
        29: 'Children crossing', 30: 'Bicycles crossing', 31: 'Beware of ice/snow', 32: 'Wild animals crossing',
        33: 'End speed + passing limits', 34: 'Turn right ahead', 35: 'Turn left ahead', 36: 'Ahead only',
        37: 'Go straight or right', 38: 'Go straight or left', 39: 'Keep right', 40: 'Keep left',
        41: 'Roundabout mandatory', 42: 'End of no passing', 43: 'End no passing veh > 3.5 tons'
    }
    return model, classes

model, classes = load_model_and_classes()

# App UI
st.title("🚦 Traffic Sign Recognition System")
st.markdown("Upload a traffic sign image, and the model will predict its class.")   

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Show image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True) 

    # Preprocess
    resized = image.resize((30, 30))
    img_array = np.expand_dims(np.array(resized), axis=0)

    # Predict
    preds = model.predict(img_array)
    pred_class = np.argmax(preds, axis=1)[0] + 1
    pred_label = classes[pred_class]

    st.success(f"### 🧠 Predicted Sign: {pred_label}")


st.markdown("Developed by: Muhammad Sohaib")