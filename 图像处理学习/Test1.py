# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 17:43:04 2018

@author: Xiaopeng
"""
import numpy as np
from skimage import io,data
#img = io.imread('C:\\Users\\Xiaopeng\\Desktop\\test.jpg',as_grey=True)
#io.imshow(img)
img1 = data.coffee()
io.imshow(img1)
#输出coffee图片中G通道的像素值
pixel = img1[1,1,1]
print('输出的像素值为%s'%pixel)
#显示红色单通道的图片
print('显示红色单通道图片')
R = img1[:,:,0]
io.imsave('C:\\Users\\Xiaopeng\\Desktop\\Picture\\coffeeR.jpg',R)
#显示绿色单通道的图片
print('显示绿色单通道图片')
G = img1[:,:,1]
io.imsave('C:\\Users\\Xiaopeng\\Desktop\\Picture\\coffeeG.jpg',G)
#显示蓝色单通道的图片
print('显示蓝色单通道图片')
B = img1[:,:,2]
io.imsave('C:\\Users\\Xiaopeng\\Desktop\\Picture\\coffeeB.jpg',B)
print('打印图片的大小，通道数')
print(img1.shape)
rows,cols,dims = img1.shape
for i in range(5000):
    x = np.random.randint(0,rows)
    y = np.random.randint(0,cols)
    img1[x,y,:] = 255
io.imshow(img1)
 