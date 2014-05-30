from sklearn.svm import SVC
import numpy as np
import matplotlib as plt
import pylab as pl

from sklearn.svm import SVC
clf = SVC(kernel='linear')

fh_train = open("train3.csv", 'r',1)
fh_test = open("test_3.csv", 'r',1)
X_train = list()
Y_train = list()
X_test = list()
Y_test = list()
while True:
	print 'one'	
	line = fh_train.readline()
	vect = list()
	if not line:
		break
	vect = line.split(",")
	print len(vect)	
	#print vect[0:1]	
	
	if vect[0] == 'pos':	
		Y_train.append(int(1))
	else:
		Y_train.append(int(0))	
	vect = map(int, vect[1:])
		
	X_train.append(vect[1:])
	#print len(vect)

print X_train[1]			
while True:
	print 'two'	
	line = fh_test.readline()
	vect = list()
	
	if not line:
		break
	vect = line.split(",")
	if vect[0] == 'pos':	
		Y_test.append(int(1))
	else:
		Y_test.append(int(0))	
	vect = map(int, vect[1:])
		
	X_test.append(vect[1:])

print len(X_train)
print len(Y_train)
#print X_train
#print len(X_train), len(Y_train), len(X_test), len(Y_test)

X = np.array(X_train)
Y = np.array(Y_train)
x = np.array(X_test)

clf.fit(X, Y) 

results = clf.predict(x)
results = map(int, results)
for item in range(0, len(results)):
	print results[item],"\t",Y_test[item]

target_names = ['0', '1']
from sklearn.metrics import classification_report
print(classification_report(Y_test, results, target_names=target_names))
