#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"
from sklearn.naive_bayes import GaussianNB
import numpy as np



X=np.array([[9,9],[9.2,9.2],[9.6,9.2],[9.2,9.2],[6.7,7.1],[7,7.4],[7.6,7.5],
   [7.2,10.3], [7.3,10.5], [7.2,9.2], [7.3,10.2], [7.2,9.7], [7.3,10.1], [7.3,10.1]])
Y=np.array([1,1,1,1,1,1,1,
   2,2,2,2,2,2,2])


model = GaussianNB()
model.fit(X,Y)
print(model.class_prior_ )
print(model.get_params() )



#Predict Output
x_test=np.array([[8,8],[8.3,8.3]])
predicted= model.predict(x_test)
print(predicted)
print(model.predict_proba(x_test))


