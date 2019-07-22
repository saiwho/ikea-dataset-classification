import os
import random
import shutil
import sys

currentpath = os.getcwd()
frompath = os.path.join(currentpath,'data', 'train')
topath = os.path.join(currentpath,'data', 'valid')

for i in os.listdir(frompath):
	randpick = random.sample(os.listdir(os.path.join(frompath,i)),100)
	for j in randpick:
		shutil.move(os.path.join(frompath,i,j), os.path.join(topath,i,j))
