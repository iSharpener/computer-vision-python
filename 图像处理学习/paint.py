# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 21:57:28 2018

@author: Xiaopeng
"""
#根据标签值对图片进行着色
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]="3"
from skimage import io,data,color
import numpy as np
img = data.coffee()
gray = color.rgb2gray(img)
io.imshow(gray)
rows,cols = gray.shape
labels = np.zeros([rows,cols])
for i in range(rows):
    for j in range(cols):
        if gray[i,j]<0.4:
            labels[i,j]=0
        elif gray[i,j]<0.75:
            labels[i,j]=1
        else:
            labels[i,j]=2
dst = color.label2rgb(labels)
io.imshow(dst)
            
