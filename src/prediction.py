#!/usr/bin/env python3
import numpy as np
import tensorflow as tf



def predict(model, features_array):
    features_tensor = tf.convert_to_tensor(features_array)
    prediction = model(features_tensor)
    return int(prediction[0])
