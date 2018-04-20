# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 20:20:05 2018

@author: Xiaopeng
"""

import cv2
import numpy as np
#随机生成500个椒盐
def salt(image):
    rows,cols,dips = image.shape
    for i in range(3000):
        x = np.random.randint(0,rows)
        y = np.random.randint(0,cols)
        image[x,y,:] = 255
    return image
def standard(image):
    grayimg = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    rows,cols = grayimg.shape
#    grayimg = float(grayimg)
    grayimg = grayimg/255.0
    averge = grayimg.mean()
    averge = round(averge,2)
    print(averge)
    s = 0
    for i in range(rows):
        for j in range(cols):
            s += pow((grayimg[i,j]-averge),2)
    stan2 = s/(rows*cols)
    print(rows,cols)
    return stan2
def gaussfilter(image):
    rows,cols,dips = image.shape
 #   dealimage = np.array(image)
if __name__=='__main__':
    img = cv2.imread('C:\\Users\\Xiaopeng\\Desktop\\Picture\\tu.jpg')
    cv2.namedWindow('original',cv2.WINDOW_NORMAL)
    cv2.imshow('original',img)
    saltimage = salt(img)
    cv2.namedWindow('saltimage',cv2.WINDOW_NORMAL)
    cv2.imshow('saltimage',saltimage)
    stan2 = standard(saltimage)
    print('方差：',stan2)
#    cv2.namedWindow('newimage',cv2.WINDOW_NORMAL)
#    cv2.imshow('newimage',newimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()