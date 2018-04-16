# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 21:26:45 2018

@author: Xiaopeng
"""

import matplotlib.pyplot as plt
from skimage import io,data,color
img = data.chelsea()
#将图片转换为HSV颜色空间
hsv = color.rgb2lab(img)
fig,axes = plt.subplots(2,2,figsize=(7,6))  
ax0,ax1,ax2,ax3 = axes.ravel()

ax0.imshow(img)
ax0.set_title('Original image')

ax1.imshow(hsv[:,:,0],cmap = plt.cm.gray)
ax1.set_title('L')

ax2.imshow(hsv[:,:,1],cmap = plt.cm.gray)
ax2.set_title('A')

ax3.imshow(hsv[:,:,2],cmap = plt.cm.gray)
ax3.set_title('B')
for ax in axes.ravel():
    ax.axis('off')
fig.tight_layout()

