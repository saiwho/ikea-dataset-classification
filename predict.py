import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

import cv2
import numpy as np
from keras.models import load_model
import sys
import os

from sklearn.metrics import accuracy_score, confusion_matrix


model = load_model('5epochs.h5')

testimglist = os.listdir(os.path.join(os.getcwd(),'data', 'test', 'test_images'))

os.chdir(os.path.join(os.getcwd(),'data', 'test', 'test_images'))
out = ""

y_hat = []
y = []
yc= []
yc_hat = []
j = 0
o = 0
for i in testimglist:
	test_img = cv2.imread(i)
	test_img = cv2.resize(test_img, (128,128))
	test_img = np.reshape(test_img, [1, 128, 128, 3])
	
	output = model.predict(test_img)
	
	if output[0][0] == 1.0:
		out = "bed"
		o = 0
	elif output[0][1] == 1.0:
		out = "chair"
		o = 1
	elif output[0][2] == 1.0:
		out = "dinnerware"
		o = 2
	elif output[0][3] == 1.0:
		out = "wardrobe"
		o = 3

	if i[:2] == 'be':
		u = 0
		p = "bed"
	elif i[:2] == 'ch':
		u = 1
		p = "chair"
	elif i[:2] == 'di':
		u = 2
		p = "dinnerware"
	elif i[:2] == 'wa':
		u = 3
		p = "wardrobe"

	y_hat.append(o)
	y.append(u)
	yc.append(p)
	yc_hat.append(out)
	print(output, i + " ------------> " + out)
	j+=1

print(accuracy_score(y, y_hat))
print(confusion_matrix(yc, yc_hat, labels=["bed", "chair", "dinnerware", "wardrobe"]))

