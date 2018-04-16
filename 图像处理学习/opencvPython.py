# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 13:33:16 2018

@author: Xiaopeng
"""

import cv2
img = cv2.imread('C:\\Users\\Xiaopeng\\Desktop\\Picture\\test.jpg')
img2 = cv2.imread('C:\\Users\\Xiaopeng\\Desktop\\Picture\\coffee.jpg')
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
if cv2.waitKey(1)&0xFF == ord('s'):
    cv2.imshow('image',img2)
    cv2.destroyAllWindows()


