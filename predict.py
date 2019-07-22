import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

import cv2
import numpy as np
from keras.models import load_model
import os
from sklearn.metrics import accuracy_score, confusion_matrix


model = load_model('20epochs.h5')

testimgtags = os.listdir(os.path.join(os.getcwd(),'data', 'test'))

os.chdir(os.path.join(os.getcwd(),'data', 'test'))


# testimgarr = np.empty((0, 128, 128, 3), dtype="uint8")

yc= []
yc_hat = []

for i in testimgtags:
	testimg = cv2.imread(i)
	testimg = cv2.resize(testimg, (128, 128))
	testimg = np.reshape(testimg, [1]+list(testimg.shape))
	
	y_hat = model.predict_proba(testimg/255.0)
	# testimgarr = np.append(testimgarr, testimg, axis=0)
	
	index = np.argmax(y_hat, axis = 1)
	prob = np.amax(y_hat, axis = 1)
	if index == 0:
		label = "bed"
		yc_hat.append(0)
	elif index == 1:
		label = "chair"
		yc_hat.append(1)
	elif index == 2:
		label = "dinnerware"
		yc_hat.append(2)
	elif index == 3:
		label = "wardrobe"
		yc_hat.append(3)

	if i[:2] == 'be':
		yc.append(0)
	elif i[:2] == 'ch':
		yc.append(1)
	elif i[:2] == 'di':
		yc.append(2)
	elif i[:2] == 'wa':
		yc.append(3)

	finallabel = "{}: {:.3f}%".format(label, prob[0]*100.0)
	finaloutimg = cv2.putText(cv2.imread(i),finallabel, (25,50), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
	cv2.imshow('output', finaloutimg)
	cv2.waitKey(2500)
	
cv2.destroyAllWindows()
print("Accuracy: %.2f " %(accuracy_score(yc, yc_hat)*100.0))


# scores = model.evaluate(x_test, y_test, verbose=1)
# print('Test loss:', scores[0])
# print('Test accuracy:', scores[1])

