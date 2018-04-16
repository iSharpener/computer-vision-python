# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 20:49:33 2018

@author: Xiaopeng
"""

from skimage import data,io,img_as_float,img_as_ubyte
import numpy as np
img = data.chelsea()
r = img[:,:,0]>170
img[r] = [0,255,0]
io.imsave('C:\\Users\\Xiaopeng\\Desktop\\Picture\\coffeeChangeR.jpg',img)
print('图片存储类型为%s'%img.dtype.name)
#unit8转float
dst = img_as_float(img)
print('转换格式之后的图片存储类型%s'%dst.dtype.name)
#float转unit8
img = np.array([0,0.5,1],dtype = float)
dst = img_as_ubyte(img)
print('转换格式之后的图片存储类型%s'%dst.dtype.name)


