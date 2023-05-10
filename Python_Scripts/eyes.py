import tensorflow as tf
from tensorflow.keras.preprocessing import image as kp_image
from tensorflow.keras.applications.vgg16 import preprocess_input
import cv2
import numpy as np

# Create a VideoCapture object to read frames from OBS stream
cap = cv2.VideoCapture('udp://@:5000')

# Get the video writer object to write the processed video to disk
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# Load a pre-trained image classification model
model = tf.keras.applications.VGG16(weights='imagenet', include_top=True)

# Loop over frames from the video stream
while True:
    # Read the next frame from the stream
    ret, frame = cap.read()

    # Process the frame
    x = kp_image.img_to_array(frame)
    x = preprocess_iEnput(x)
    x = tf.keras.applications.vgg16.preprocess_input(x)
    x = tf.image.resize(x, (224, 224))
    x = tf.expand_dims(x, axis=0)
    preds = model.predict(x)

    # Write the processed frame to disk
    out.write(frame)

    # Display the frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
