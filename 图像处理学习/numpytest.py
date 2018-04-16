# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 14:02:47 2018

@author: Xiaopeng
"""
import cv2
import numpy
import os
img = numpy.zeros((3,3),dtype=numpy.ubyte)
print(img)
img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = numpy.array(randomByteArray)
grayImage = flatNumpyArray.reshape(300,400)
bgrImage = flatNumpyArray.reshape(200,200,3)
cv2.imshow('randomImage',bgrImage)
cv2.waitKey()
cv2.destroyAllWindows()


