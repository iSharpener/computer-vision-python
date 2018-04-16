# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 20:15:14 2018

@author: Xiaopeng
"""

import numpy as np
from skimage import io,data,color
img = data.coffee()
cutp = img[100:200,300:400,:]
#裁剪图片
io.imsave('C:\\Users\\Xiaopeng\\Desktop\\Picture\\coffeeCut.jpg',cutp)
#对图片特定部分赋值
img[40:70,:] = img[350:380,:]
io.imsave('C:\\Users\\Xiaopeng\\Desktop\\Picture\\coffee=.jpg',img)

#对图片进行二值化
picture = data.immunohistochemistry()
img_grey = color.rgb2grey(picture)
print(img_grey.shape)
rows,cols = img_grey.shape
for i in range(rows):
    for j in range(cols):
        if img_grey[i,j]<=0.5:
            img_grey[i,j]=0
        else:
            img_grey[i,j]=1
io.imshow(img_grey)
io.imsave('C:\\Users\\Xiaopeng\\Desktop\\Picture\\separate.jpg',img_grey)

