from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(11)

buf = ''

while True:
	# Grab the webcamera's image.
	ret, image = camera.read()

	# Resize the raw image into (224-height,224-width) pixels
	image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

	# Make the image a numpy array and reshape it to the models input shape.
	image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

	# Normalize the image array
	image = (image / 127.5) - 1

	# Predicts the model
	prediction = model.predict(image, verbose=0)
	index = np.argmax(prediction)
	class_name = class_names[index]
	confidence_score = prediction[0][index]

	# Print prediction and confidence score
	if buf == class_name[2:]:
		counter = counter + 1
	else:
		counter = 0

	if counter == 5:
		print(class_name[2:], end='')
		counter = 0

	buf = class_name[2:]

camera.release()
