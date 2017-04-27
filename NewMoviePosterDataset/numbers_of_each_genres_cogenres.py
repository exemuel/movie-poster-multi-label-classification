import h5py


f = h5py.File('./Documents/NewMoviePosterDataset/dataset.h5')
y = f['y'].value
f.close()

v1 = [tuple(row) for row in y]

v2 = []

for i in v1:
	if i not in v2:
		v2.append(i)

v3 = [0] * len(v2)

for j in range(len(v1)):
	for i in range(len(v2)):
		if v1[j] == v2[i]:
			v3[v2.index(v1[j])] = v3[v2.index(v1[j])] + 1

genres = ['action','adventure', 'animation', 'biography', 'comedy', 'crime' , 'drama', 'family', 'fantasy', 'film-noir', 'history', 'horror', 'music', 'musical', 'mystery', 'romance', 'sci-fi', 'sport', 'thriller', 'war', 'western']

v4 = []

for j in range(len(v2)):
	tv = []
	for i in range(len(v2[j])):
		if v2[j][i] == 1:
			tv.append(genres[i])
	v4.append(tv)
			

thefile = open('./Documents/NewMoviePosterDataset/output.txt', 'w')
for i in range(len(v4)):
	nstring = str(v4[i]) + ' ' + str(v3[i])
	print>>thefile, nstring
thefile.close()
