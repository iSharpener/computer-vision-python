# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 21:44:22 2018

@author: Xiaopeng
"""

import cv2
import numpy as np
#随机生成500个椒盐
def salt(image):
    rows,cols,dips = image.shape
    for i in range(1000):
        x = np.random.randint(0,rows)
        y = np.random.randint(0,cols)
        image[x,y,:] = 255
    return image
def avergefilter(image):
    rows,cols,dips = image.shape
    dealimage = np.array(image,dtype = np.uint16)
    for i in range(1,rows-1):
        print(i)
        for j in range(1,cols-1):
            averge0 = round((dealimage[i-1,j-1,0]+dealimage[i-1,j,0]+dealimage[i-1,j+1,0]+dealimage[i,j-1,0]+dealimage[i,j,0]+dealimage[i,j+1,0]+dealimage[i+1,j-1,0]+dealimage[i+1,j,0]+dealimage[i+1,j+1,0])/9)
            averge1 = round((dealimage[i-1,j-1,1]+dealimage[i-1,j,1]+dealimage[i-1,j+1,1]+dealimage[i,j-1,1]+dealimage[i,j,1]+dealimage[i,j+1,1]+dealimage[i+1,j-1,1]+dealimage[i+1,j,1]+dealimage[i+1,j+1,1])/9)
            averge2 = round((dealimage[i-1,j-1,2]+dealimage[i-1,j,2]+dealimage[i-1,j+1,2]+dealimage[i,j-1,2]+dealimage[i,j,2]+dealimage[i,j+1,2]+dealimage[i+1,j-1,2]+dealimage[i+1,j,2]+dealimage[i+1,j+1,2])/9)
            
            dealimage[i,j,0] = averge0
            dealimage[i,j,1] = averge1
            dealimage[i,j,2] = averge2
    dealimage = np.array(dealimage,dtype = np.uint8)
    return dealimage
if __name__=='__main__':
    img = cv2.imread('C:\\Users\\Xiaopeng\\Desktop\\Picture\\tu.jpg')
    cv2.namedWindow('original',cv2.WINDOW_NORMAL)
    cv2.imshow('original',img)
    saltimage = salt(img)
    cv2.namedWindow('saltimage',cv2.WINDOW_NORMAL)
    cv2.imshow('saltimage',saltimage)
    newimg = avergefilter(saltimage)
    cv2.namedWindow('newimage',cv2.WINDOW_NORMAL)
    cv2.imshow('newimage',newimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()