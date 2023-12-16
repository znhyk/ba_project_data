import tensorflow as tf

# Load the Keras model from the H5 file
model = tf.keras.models.load_model('C:/Users/koung/kicpython/hansik/kfood_new/models/model.h5')

# Convert the Keras model to a TFLite model
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TFLite model to a file
with open('C:/Users/koung/kicpython/hansik/kfood_new/Tflite/model.tflite', 'wb') as f:
    f.write(tflite_model)