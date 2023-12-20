# import the libraries
import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model('convnet_from_scratch_original_data.h5')

converter = tf.lite.TFLiteConverter.from_keras_model(model)

tflite_model = converter.convert()

with open('convnet_from_scratch_original_data.tflite', 'wb') as f_out:
    f_out.write(tflite_model)
