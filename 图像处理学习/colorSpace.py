# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 21:48:49 2018

@author: Xiaopeng
"""

from skimage import io,data,color
img = data.chelsea()
hsv = color.convert_colorspace(img,'RGB','HSV')
io.imshow(hsv)
