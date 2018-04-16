# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 14:15:37 2018

@author: Xiaopeng
"""

import cv2
img = cv2.imread("C:\\Users\\Xiaopeng\\Desktop\\Picture\\coffee.jpg")
cv2.imwrite('C:\\Users\\Xiaopeng\\Desktop\\Picture\\coffee.png',img)
print('success')
grayimg = cv2.imread("C:\\Users\\Xiaopeng\\Desktop\\Picture\\coffee.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imwrite('grayCoffee.png',grayimg)
cv2.imshow('grayimg',grayimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
print('success')