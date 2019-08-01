import os
import re
import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input



# to save space in the CSV, only track non-zero values in the features;
# full lists can be reconstructed later
def nonzeroes(arr, filtered):
    for idx, item in enumerate(arr):
        if type(item) is np.ndarray:
            filtered[idx] = nonzeroes(item, dict())
        else:
            if item != 0:
                filtered[idx] = item
    return filtered


data_arr = []

def upload_nn(upload_img, data_df):
	model = VGG16(weights='imagenet', include_top=False)
	img_dict = {}
	img = image.load_img(upload_img, target_size=(224,224))
	img_data = image.img_to_array(img)
	img_data = np.expand_dims(img_data, axis=0)
	img_data = preprocess_input(img_data)
	features = model.predict(img_data)
	img_dict['FEATURES'] = nonzeroes(features, dict())
	data_arr.append(img_dict)
	data_df = pd.DataFrame(data_arr)
	data_df = data_df['FEATURES'].iloc[0]
	print(data_df)
	return data_df