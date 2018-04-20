# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 19:55:48 2018

@author: Xiaopeng
"""

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
    for i in range(3000):
        x = np.random.randint(0,rows)
        y = np.random.randint(0,cols)
        image[x,y,:] = 255
    return image
def middlefilter(image):
    rows,cols,dips = image.shape
    dealimage = np.array(image)
    for i in range(1,rows-1):
      #  print(i)
        for j in range(1,cols-1):
            for m in range(dips):
                box = list()
                box.append(image[i-1,j-1,m])
                box.append(image[i-1,j,m])
                box.append(image[i-1,j+1,m])
                box.append(image[i,j-1,m])
                box.append(image[i,j,m])
                box.append(image[i,j+1,m])
                box.append(image[i+1,j-1,m])
                box.append(image[i+1,j,m])
                box.append(image[i+1,j+1,m])
                box = sorted(box)
                dealimage[i,j,m] = box[4]
    return dealimage
if __name__=='__main__':
    img = cv2.imread('C:\\Users\\Xiaopeng\\Desktop\\Picture\\coffee.jpg')
    cv2.namedWindow('original',cv2.WINDOW_NORMAL)
    cv2.imshow('original',img)
    saltimage = salt(img)
    cv2.namedWindow('saltimage',cv2.WINDOW_NORMAL)
    cv2.imshow('saltimage',saltimage)
    newimg = middlefilter(saltimage)
    cv2.namedWindow('newimage',cv2.WINDOW_NORMAL)
    cv2.imshow('newimage',newimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()