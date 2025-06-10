from tensorflow.keras.models import load_model
import numpy as np
from utils.preprocess import preprocess_image

# Define class names here directly
CLASS_NAMES = ['covid19', 'pneumonia', 'tuberculosis', 'normal']

def load_trained_model(model_path):
    return load_model(model_path)

def predict_image(model, img_path):
    img_array = preprocess_image(img_path)
    preds = model.predict(img_array)
    class_idx = np.argmax(preds, axis=1)[0]
    return CLASS_NAMES[class_idx], preds[0]