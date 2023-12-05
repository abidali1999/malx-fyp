import tensorflow as tf
# Load the Keras model
model = tf.keras.models.load_model('/home/abidali1999063/m192_v3.h5',compile=False)
# Convert the model to TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
# Save the TensorFlow Lite model to a .tflite file
with open('/home/abidali1999063/m192_v3.tflite', 'wb') as f:
    f.write(tflite_model)
