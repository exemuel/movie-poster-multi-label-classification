import numpy as np
import h5py
import cv2
import scipy.io as sio
import os
from skimage import io
from skimage.transform import resize


label_path = './Documents/NewMoviePosterDataset/exemuel/postergenres.mat'	# target labels
id_path = './Documents/NewMoviePosterDataset/exemuel/posterid.mat'			# target ids
image_path = './Documents/NewMoviePosterDataset/exemuel/Posters'			# images

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
	img = cv2.resize(img,(100,100))
	#img = img.transpose((2,0,1))
	x.append(img)
	
x = np.array(x)
f = h5py.File('./Documents/exemuel/MoviePosterClassification1.0/dataset.h5')
f['x'] = x
f['y'] = y
f.close()
