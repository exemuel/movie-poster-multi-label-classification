import os, os.path

# path joining version for other paths
DIR = './Documents/NewMoviePosterDataset/Original'
print len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

#########################################################################################

#import scipy.io
#mat = scipy.io.loadmat('./Documents/SecondMoviePoster/poster_genres.mat')
#scipy.io.savemat('test.mat',mat)
