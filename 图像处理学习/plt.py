# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 12:55:48 2018

@author: Xiaopeng
"""
from skimage import data
import matplotlib.pyplot as plt
img = data.chelsea()
#创建一个名为astronaut的窗口，并且设置大小
plt.figure(num='astronaut',figsize=(8,8))
#将窗口分为两行两列四个子图，可以显示四幅图片
plt.subplot(2,2,1)
plt.title('origin image')
plt.imshow(img)

#显示第二个子图
plt.subplot(2,2,2)
plt.title('R channel')
plt.imshow(img[:,:,0],plt.cm.gray)
plt.axis('off')

#第三个子图
plt.subplot(2,2,3)
plt.title('G channel')
plt.imshow(img[:,:,1],plt.cm.gray)
plt.axis('off')
#第四张图
plt.subplot(2,2,4)
plt.title('B channel')
plt.imshow(img[:,:,2],plt.cm.gray)
plt.axis('off')

plt.show()