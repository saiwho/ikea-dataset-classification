import os 
import sys

try:
	dirname = sys.argv[1]

	imgdirpath = os.path.join(os.getcwd(),'data',dirname)

	for i in os.listdir(imgdirpath):
		x = 1 if dirname=='train' else 401
		for j in os.listdir(os.path.join(imgdirpath,i)):
			os.rename(os.path.join(imgdirpath,i,j), os.path.join(imgdirpath,i,i+str(x)+'.jpg'))
			x += 1


except IndexError as e:
	print('Exception Occured: ', e)

