import numpy as np
import h5py
import cv2
import scipy.io as sio
import os
from skimage import io
from skimage.transform import resize


label_path = './Documents/SecondMoviePoster/postergenres.mat'	# target labels
id_path = './Documents/SecondMoviePoster/posterid.mat'			# target ids
image_path = './Documents/SecondMoviePoster/Original'			# images

x = []

y = sio.loadmat(label_path)
y = y['genres']

z = sio.loadmat(id_path)
z = z['imdbids']

for i in range(len(z)):
	try:
		print 'reading image: ' + str(z[i]) + '.jpg'
		filename = image_path + "/" + str(z[i]) + '.jpg'
	except TypeError:
		print 'reading image: ' + str(z[i]) + '.png'
		filename = image_path + "/" + str(z[i]) + '.png'
		
	img = cv2.imread(filename)
	res_img = img.reshape((-1, 3))
	
	# convert to np.float32
	res_img = np.float32(res_img)
	
	# define criteria, number of clusters(K) and apply kmeans()
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
	k = 10
	ret, label, center = cv2.kmeans(res_img, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
	
	# convert back into uint8, and make original image
	center = np.uint8(center)
	res = center[label.flatten()]
	res2 = res.reshape((img.shape))
	
	img = cv2.resize(res2,(100,100))
	#img = img.transpose((2,0,1))
	x.append(img)
	
x = np.array(x)
f = h5py.File('./Documents/FourthMoviePoster/dataset.h5')
f['x'] = x
f['y'] = y
f.close()
