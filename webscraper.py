from bs4 import BeautifulSoup
import requests
import urllib.request	
import os
import sys

j = 749
k = 1

os.chdir(os.path.join(os.getcwd(),'x'))

while k<2:

	if k == 1:
		result = requests.get('https://www.ikea.com/gb/en/cat/side-plates-18863/')
	else:
		result = requests.get("https://www.ikea.lv/en/products/bedroom/wardrobes/system-wardrobes?&name[]=PAX&page="+str(k))	

	src = result.content	

	soup = BeautifulSoup(src, 'html.parser')
	# soup = BeautifulSoup(src, 'lxml')
	divtags = soup.find_all("img")
	# print(divtags)
	# sys.exit(0)
	for i in divtags:
		if "JPG" in i.attrs['src']:
			print(j, str(i.attrs['src']))			
			urllib.request.urlretrieve(str(i.attrs['src']), str(j)+'.jpg')
			j += 1
	k += 1

