import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from PIL import Image

def get_img_array(img_path, size):
    img = Image.open(img_path).convert('RGB').resize(size)
    array = np.array(img) / 255.0
    return np.expand_dims(array, axis=0)

def make_gradcam_heatmap(img_array, model, last_conv_layer_name, pred_index=None):
    # Ensure the model is built
    if not model.built:
        model.build(img_array.shape)
    # Check if the layer exists
    try:
        last_conv_layer = model.get_layer(last_conv_layer_name)
    except ValueError:
        raise ValueError(
            f"Layer '{last_conv_layer_name}' not found in model. "
            f"Available layers: {[layer.name for layer in model.layers]}"
        )
    grad_model = tf.keras.models.Model(
        [model.inputs], [last_conv_layer.output, model.output]
    )
    with tf.GradientTape() as tape:
        conv_outputs, predictions = grad_model(img_array)
        if pred_index is None:
            pred_index = tf.argmax(predictions[0])
        class_channel = predictions[:, pred_index]
    grads = tape.gradient(class_channel, conv_outputs)
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
    conv_outputs = conv_outputs[0]
    heatmap = conv_outputs @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)
    heatmap = tf.maximum(heatmap, 0) / tf.math.reduce_max(heatmap)
    return heatmap.numpy()