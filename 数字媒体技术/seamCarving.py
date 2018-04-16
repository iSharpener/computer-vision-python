# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 13:06:51 2018

@author: Xiaopeng
"""
from skimage import filters,feature
import cv2
import numpy
def minofLine(i,image,newcol):
    row,col,dip = img.shape
   # print(row,' ',col,' ',dip)
    min = image[i,1]
   # print('初始的min值为',min)
    minloc = 1
    for j in range(1,newcol-1):
        if image[i,j]<min:
            min = image[i,j]
            minloc = j
  #  print('min',minlocation)
    return min,minloc
def minof2(a,b):
    if a < b:
        return -1,0
    else:
        return -1,1
def minof2right(a,b):
    if a < b:
        return -1,0
    else:
        return -1,-1
def minof3(a,b,c):
    if a>=b and b>=c:
        return -1,1
    if a>=c and c>=b:
        return -1,0
    if b>=a and a>=c:
        return -1,1
    if b>=c and c>=a:
        return -1,-1
    if c>=a and a>=b:
        return -1,0
    if c>=b and b>=a:
        return -1,-1
            
def minseam(i,minlocation,image):
    row,col = image.shape
    times = row-3
    j = 0
    #最后一行的最小值点在(i,minlocation)
    seam = dict()
    seam[i] = minlocation
    while j < times:
       # print(minlocation==col-2)
        if minlocation == 1:
            one,two = minof2(image[i-1,minlocation],image[i-1,minlocation+1])
            i = i+one
            minlocation = minlocation+two
            seam[i] = minlocation
         #   print('location:','(%f,%f)'%(i,minlocation))
        elif minlocation == col-2:
            one,two = minof2right(image[i-1,minlocation],image[i-1,minlocation-1])
            i = i+one
            minlocation = minlocation+two
            seam[i] = minlocation
         #   print('location','(%f,%f)'%(i,minlocation))
        else:
            one,two = minof3(image[i-1,minlocation-1],image[i-1,minlocation],image[i-1,minlocation+1])
            i = i+one
            minlocation = minlocation+two
            seam[i] = minlocation
         #   print('location','(%f,%f)'%(i,minlocation))
        j+=1 
    return seam
img = cv2.imread('C:\\Users\\Xiaopeng\\Desktop\\Picture\\test1.jpg')
originalimage = img.copy()
imggray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
tigray = filters.sobel(imggray)
row,col,dip = img.shape
print(row,' ',col,' ',dip)

#寻找最小的能量线
copyimage = tigray.copy()
widthcut = input('请输入宽度缩小度：\n')
widthcut = int(widthcut)
i = 0
while i<widthcut:
    min,minlocation = minofLine(row-2,copyimage,col-i)
   # copyimage[row-2,minlocation] = 1
    print('第',i,'次裁剪',min,' ',row-2,' ',minlocation)
    seam = minseam(row-2,minlocation,copyimage)
    for key in seam:
        tigray[key,seam[key]] = 1
    for key in seam:
#        img[key-1,seam[key]] = (img[key-1,seam[key]]+img[key,seam[key]])/2
#        img[key+1,seam[key]] = (img[key+1,seam[key]]+img[key,seam[key]])/2
        for m in range(seam[key],col-i-1):
            img[key,m] = img[key,m+1]
            if m==col-i-2:
                img[key,m]=255
            copyimage[key,m] = copyimage[key,m+1]
            if m==col-i-2:
                copyimage[key,m] = 1
    #    print('key:',key,'value:',seam[key])
       # img[key,seam[key]] = 255
        
    i+=1
    
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.namedWindow('originalimage',cv2.WINDOW_NORMAL)
cv2.imshow('originalimage',originalimage)
#cv2.namedWindow('original',cv2.WINDOW_)
cv2.namedWindow('copyimage',cv2.WINDOW_NORMAL)
cv2.imshow('copyimage',tigray)
cv2.imwrite('C:\\Users\\Xiaopeng\\Desktop\\Picture\\picture1.JPG',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
