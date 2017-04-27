import os
import json
import shutil
import os.path
import scipy.io
import numpy as np
import scipy as sp

from shutil import copyfile

genres = ['action','adventure', 'animation', 'biography', 'comedy', 'crime' , 'drama', 'family', 'fantasy', 'film-noir', 'history', 'horror', 'music', 'musical', 'mystery', 'romance', 'sci-fi', 'sport', 'thriller', 'war', 'western']
#genres = ['action']
#data = {'genres': np.transpose(np.array([genres], dtype=np.object))}
#sio.savemat('./Documents/exemuel/NewMoviePosterDataset/class_name.mat', data)

poster_ids = []
poster_genres = []

gdir = './Documents/exemuel/NewMoviePosterDataset/Posters'
if not os.path.exists(gdir):
	os.makedirs(gdir)
else:
	shutil.rmtree(gdir)
	os.makedirs(gdir)
	
for g in genres:
	filename = './Documents/exemuel/NewMoviePosterDataset/Metadata/' + g + '.json'
	with open(filename) as data_file:
		data = json.load(data_file)
	
	for i in range(len(data)):
		t_ids = data[i]['imdbID']
		t_genres = data[i]['genre']
		xt_genre = t_genres.split(', ')
		
		if t_ids in poster_ids:
			pass
		else:
			src_imagefn = './Documents/exemuel/NewMoviePosterDataset/ClassifiedPosters/' + g + '/' + t_ids + '.jpg'
			dst_imagefn = './Documents/exemuel/NewMoviePosterDataset/Posters/' + t_ids + '.jpg'
			
			if os.path.isfile(src_imagefn):
				a = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
				
				if 'Action' in xt_genre:
					b = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
					a = np.array(a) + np.array(b)
				
				if 'Adventure' in xt_genre:
					b = [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
					a = np.array(a) + np.array(b)
					
				if 'Animation' in xt_genre:
					b = [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
					a = np.array(a) + np.array(b)
				
				if 'Biography' in xt_genre:
					b = [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
					a = np.array(a) + np.array(b)
				
				if 'Comedy' in xt_genre:
					b = [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
					a = np.array(a) + np.array(b)
					
				if 'Crime' in xt_genre:
					b = [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
					a = np.array(a) + np.array(b)
					
				if 'Drama' in xt_genre:
					b = [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
					a = np.array(a) + np.array(b)
				
				if 'Family' in xt_genre:
					b = [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
					a = np.array(a) + np.array(b)
				
				if 'Fantasy' in xt_genre:
					b = [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
					a = np.array(a) + np.array(b)
					
				if 'Film-Noir' in xt_genre:
					b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
					a = np.array(a) + np.array(b)
				
				if 'History' in xt_genre:
					b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
					a = np.array(a) + np.array(b)
				
				if 'Horror' in xt_genre:
					b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
					a = np.array(a) + np.array(b)
				
				if 'Music' in xt_genre:
					b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
					a = np.array(a) + np.array(b)
				
				if 'Musical' in xt_genre:
					b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0]
					a = np.array(a) + np.array(b)
					
				if 'Mystery' in xt_genre:
					b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0]
					a = np.array(a) + np.array(b)
				
				if 'Romance' in xt_genre:
					b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0]
					a = np.array(a) + np.array(b)
				
				if 'Sci-Fi' in xt_genre:
					b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0]
					a = np.array(a) + np.array(b)
				
				if 'Sport' in xt_genre:
					b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0]
					a = np.array(a) + np.array(b)
				
				if 'Thriller' in xt_genre:
					b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0]
					a = np.array(a) + np.array(b)
					
				if 'War' in xt_genre:
					b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0]
					a = np.array(a) + np.array(b)
					
				if 'Western' in xt_genre:
					b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]
					a = np.array(a) + np.array(b)
					
				copyfile(src_imagefn, dst_imagefn)
				poster_ids.append(t_ids)	
				poster_genres.append(a)
			else:
				pass
			
	
data = {'imdbids': np.transpose(sp.array(poster_ids, dtype=np.str))}
sp.io.savemat('./Documents/exemuel/NewMoviePosterDataset/posterid.mat', data)

data = {'genres': sp.array(poster_genres, dtype=np.int)}
sp.io.savemat('./Documents/exemuel/NewMoviePosterDataset/postergenres.mat', data)