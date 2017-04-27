#! /usr/bin/env python
import urllib
import urllib2
import re
from bs4 import BeautifulSoup as bs
import unicodecsv as csv
import json
import pdb
import re
import sys
import os
import io
import shutil


#genres = ['action','adventure', 'animation', 'biography', 'comedy', 'crime' , 'documentary' , 'drama' , 'family', 'fantasy', 'film-noir', 'history', 'horror', 'music', 'musical', 'mystery', 'romance', 'sci-fi', 'sport', 'thriller', 'war', 'western']
genres = ['comedy']
#left behind
#genres = ['comedy', 'drama']


def get_poster(url):
	
	html = urllib2.urlopen(url)
	soup = bs(html.read(), "html.parser")
	
	tags = soup.find_all('div', class_ = "poster")
	for tag in tags:
		link = tag.find('a')['href']
		url = "http://www.imdb.com" + link
	
	return url


def get_poster2(url):
	
	html = urllib2.urlopen(url)
	soup = bs(html.read(), "html.parser")
	
	desc = soup.find_all(attrs={"itemprop":"image"})
	
	try:
		url = desc[0]['content'].encode('utf-8')
	except:
		url = 'N/A'
	
	return url

def internet_on(url):
	try:
		urllib2.urlopen(url)
		return True
	except urllib2.URLError as err:
		return False

if __name__ == '__main__':

	for genre in genres:
		
		page = 1
		imdbIDs = []
		titles = []
		durations = []
		years = []
		genres = []
		ratings = []
		directors = []
		images = []
		
		while page > 0:
			print genre + ' page ' + str(page)
			url = 'http://www.imdb.com/search/title?genres=' + genre + '&sort=user_rating,desc&title_type=feature&num_votes=500,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2406822102&pf_rd_r=10328PMYFYE70699AW2H&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&page=' + str(page)
			
			if internet_on(url) is True:				
				html = urllib2.urlopen(url)
				soup = bs(html.read(), "html.parser")
				
				# Check the availability of the result 
				lister = soup.find_all('div', class_ = 'lister-item mode-advanced')
				
				# End Criterion
				if lister != []:
					page = page + 1
					
					for li in lister:
						tags = li.find_all('div', class_ = 'ribbonize')
						for tag in tags:
							temp = tag.attrs['data-tconst']
						if temp != []:
							imdbIDs.append(temp)
						else:
							temp = 'N/A'
							imdbIDs.append(temp)
				
						tags = li.find_all('h3', class_ = 'lister-item-header')
						for tag in tags:
							temp = tag.a.text.strip()
						if temp != []:
							titles.append(temp)
						else:
							temp = 'N/A'
							titles.append(temp)
						
						tags = li.find_all('span', class_ = 'runtime')
						for tag in tags:
							temp = tag.text.strip()
						if 'min' in temp:
							durations.append(temp)
						else:
							temp = 'N/A'
							durations.append(temp)
					
						tags = li.find_all(class_ = 'lister-item-year text-muted unbold')
						for tag in tags:
							temp = tag.text.strip()
							temp = re.sub('[(?.!/;:)]', '', temp)
						if temp != []:
							years.append(temp)
						else:
							temp = 'N/A'
							years.append(temp)
											
						tags = li.find_all('span', class_ = 'genre')
						for tag in tags:
							temp = tag.text.strip()
						if temp != []:
							genres.append(temp)
						else:
							temp = 'N/A'
							genres.append(temp)
						
						tags = li.find_all('div', class_ = 'inline-block ratings-imdb-rating')
						for tag in tags:
							temp = tag.strong.text.strip()
						if temp != []:
							ratings.append(temp)
						else:
							temp = 'N/A'
							ratings.append(temp)
					
						tags = li.find_all(href = re.compile('.*adv_li_dr_0.*'))
						for tag in tags:
							temp = tag.text.strip()
						if temp != []:
							directors.append(temp)
						else:
							temp = 'N/A'
							directors.append(temp)
				
						imgs = li.find_all('div', class_ = 'lister-item-image float-left')
						for img in imgs:
							link = img.find('a')['href']
							url = "http://www.imdb.com" + link
							new_url = get_poster(url)
							new_url2 = get_poster2(new_url)
							images.append(new_url2)
				else:
					break
					
			else:
				print 'Lost connection. Please wait while the system tries to reconnect.'
				break
				
				
		# Save (Make it work for Python 2+3 and with Unicode)
		try:
			to_unicode = unicode
		except NameError:
			to_unicode = str
		
		# Save (Define data)
		data = []
		
		# Save (Write JSON file)
		for i in range(len(imdbIDs)):
			item = {'imdbID': imdbIDs[i],
					'title': titles[i],
					'duration': durations[i],
					'year': years[i],
					'genre': genres[i],
					'rating': ratings[i],
					'director': directors[i],
					'poster': images[i]}
			data.append(item)
			
		filename = './Documents/NewMoviePosterDataset/Metadata/' + genre + '.json'
		with io.open(filename, 'w', encoding='utf8') as outfile:
			str_ = json.dumps(data, indent=4, separators=(',', ':'), ensure_ascii=False)
			outfile.write(to_unicode(str_))
		
		print 'Downloading movie posters...'
			
		gdir = './Documents/NewMoviePosterDataset/ClassifiedPosters/' + genre
		if not os.path.exists(gdir):
			os.makedirs(gdir)
		else:
			shutil.rmtree(gdir)
			os.makedirs(gdir)
			
		for i in range(len(images)):
			if images[i] == 'N/A':
				pass
			else:
				f = open('./Documents/NewMoviePosterDataset/ClassifiedPosters/' + genre + '/' + imdbIDs[i] + '.jpg', 'wb')
				f.write(urllib.urlopen(images[i]).read())
				f.close()
				
