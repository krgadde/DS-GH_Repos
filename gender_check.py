# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 16:35:39 2018

@author: karun
"""

from sklearn import tree
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn import neighbors
from sklearn.naive_bayes import GaussianNB
import numpy as np


# [height, weight, shoe_size]
X=[[181, 80, 44],[177, 70, 43],[160, 60, 38],[154, 54, 37], [166, 65, 40],[190, 90, 47],[175, 64, 39],[177, 70, 40],[159, 55, 37],[171, 75, 42],[181, 85, 43]]

Y=['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female','female', 'male', 'male']

#Classifiers
clf=tree.DecisionTreeClassifier()
clf1=svm.SVC()
clf2=neighbors.KNeighborsClassifier()
clf3=GaussianNB()

#Train Model
clf=clf.fit(X,Y)
clf1=clf1.fit(X,Y)
clf2=clf2.fit(X,Y)
clf3=clf3.fit(X,Y)

_X=[[184,84,44],[198,92,48],[183,83,44],[166,47,36],[170,60,38],[172,64,39],[182,80,42],[180,80,43]]
_Y=['male','male','male','female','female','female','male','male']


#prediction
prediction=clf.predict(_X)
prediction1=clf1.predict(_X)
prediction2=clf2.predict(_X)
prediction3=clf3.predict(_X)


#Results
r=accuracy_score(_Y,prediction)
r1=accuracy_score(_Y,prediction1)
r2=accuracy_score(_Y,prediction2)
r3=accuracy_score(_Y,prediction3)

print("Tee:",r*100)
print("SVM:", r1*100)
print ("KNN:", r2*100)
print("Naive:", r3*100)

#print best result
maxValue=np.argmax([r1,r2,r3])
#print (maxValue)
classfiers={0:'SVM',1:'KNN', 2:'Naive'}
print("Best Classifier: {}".format(classfiers[maxValue]))


