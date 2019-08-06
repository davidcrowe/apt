import os
import re
import pandas as pd
import numpy as np
from numpy.linalg import norm
from ast import literal_eval
from operator import itemgetter

from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.callbacks import TensorBoard, EarlyStopping
import tensorflow as tf


def allowed_file(filename):
	return '.' in filename and \
	filename.rsplit('.', 1)[1].lower() in ALLOWED_IMAGE_EXTENSIONS


def processPhoto(photo):
	graph = tf.get_default_graph()
	model = VGG16(weights='imagenet', include_top=False)

	img = image.load_img(photo, target_size=(224,224))
	img_data = image.img_to_array(img)
	img_data = np.expand_dims(img_data, axis=0)
	img_data = preprocess_input(img_data)

	with graph.as_default():
		features = model.predict(img_data)
	return features


def fromZeroes(data):
	features = literal_eval(data)
	narray = np.zeros((1,7,7,512))

	for i, first in features.items():
		for j, second in first.items():
			for k, third in second.items():
				for l, fourth in third.items():
					narray[i][j][k][l] = fourth

	return narray


def findClosest(photo, iarray):
	photo = processPhoto(photo)
	closest = []
	for image in iarray:
		comparison = {
			'mlsnum': image.mls_num,
			'closeness': norm(photo - fromZeroes(image.features))
		}
		closest.append(comparison)


	closest.sort(key=itemgetter('closeness'))
	print(closest[0:4])
	#only return the top 5
	return [c['mlsnum'] for c in closest[:5]]


def findClosestPropDetail(property, iarray):
	closest = []
	for image in iarray:
		comparison = {
			'mlsnum': image.mls_num,
			'closeness': norm(fromZeroes(property.features) - fromZeroes(image.features))
		}
		closest.append(comparison)

	closest.sort(key=itemgetter('closeness'))
	#only return the top 5
	return [c['mlsnum'] for c in closest[:5]]









