import h5py
from sklearn.cross_validation  import train_test_split

def load():
	f = h5py.File('./Documents/exemuel/MoviePosterClassification1.0/dataset.h5')
	x = f['x'].value
	y = f['y'].value
	f.close()
	x_train , x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=100)
	return x_train, x_test, y_train, y_test
