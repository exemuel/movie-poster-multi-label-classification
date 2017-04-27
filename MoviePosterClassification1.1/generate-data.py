import numpy as np
import h5py
import cv2
import scipy.io as sio
import os
from skimage import io
from skimage.transform import resize


label_path = './Documents/exemuel/NewMoviePosterDataset/postergenres.mat'	# target labels
id_path = './Documents/exemuel/NewMoviePosterDataset/posterid.mat'			# target ids
image_path = './Documents/exemuel/NewMoviePosterDataset/Posters'			# images

x = []

y = sio.loadmat(label_path)
y = y['genres']

z = sio.loadmat(id_path)
z = z['imdbids']

for i in range(len(z)):
	try:
		print 'reading image: ' + str(z[i]) + '.jpg'
		img = image_path + "/" + str(z[i]) + '.jpg'
	except TypeError:
		print 'reading image: ' + str(z[i]) + '.png'
		img = image_path + "/" + str(z[i]) + '.png'
		
	img = cv2.imread(img)
	
	# Convert BGR to HSV
	hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	
	hue, sat, val = hsv_img[:,:,0], hsv_img[:,:,1], hsv_img[:,:,2]
	
	# create a CLAHE object (Arguments are optional).
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	clh = clahe.apply(hue)
	cls = clahe.apply(sat)
	clv = clahe.apply(val)
	
	img2 = cv2.merge((clh, cls, clv))
	
	# Convert HSV to BGR
	rgb_img = cv2.cvtColor(img2, cv2.COLOR_HSV2BGR)
	
	img = cv2.resize(rgb_img,(100,100))
	#img = img.transpose((2,0,1))
	x.append(img)
	
x = np.array(x)
f = h5py.File('./Documents/exemuel/MoviePosterClassification1.1/dataset.h5')
f['x'] = x
f['y'] = y
f.close()
