# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 22:33:46 2018

@author: Xiaopeng
"""

from skimage import data,exposure,img_as_float
import matplotlib.pyplot as plt
img = img_as_float(data.moon())
#调暗
gam1 = exposure.adjust_gamma(img,2)
#调亮
gam2 = exposure.adjust_gamma(img,0.5)
gam3 = exposure.adjust_gamma(img,3)
plt.figure('adjust_gamma',figsize=(8,8))

plt.subplot(221)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)
plt.axis('off')

plt.subplot(222)
plt.title('gamma=2')
plt.imshow(gam1,plt.cm.gray)
plt.axis('off')

plt.subplot(223)
plt.title('gamma=0.5')
plt.imshow(gam2,plt.cm.gray)
plt.axis('off')

plt.subplot(224)
plt.title('gamma=3')
plt.imshow(gam3,plt.cm.gray)
plt.axis('off')
plt.show()
