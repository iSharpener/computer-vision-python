# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 16:55:22 2018

@author: Xiaopeng
"""
from skimage import io,data_dir,color,transform
import numpy as np
str = data_dir+'//*.png'
def convert_gray(f):
    rgb = io.imread(f)
    gray = color.rgb2gray(rgb)
    dst = transform.resize(gray,(256,256))
    return gray
coll = io.ImageCollection(str,load_func=convert_gray)
print(len(coll))/Library/anaconda3/bin
for i in range(len(coll)):
    io.imsave('C:\\Users\\Xiaopeng\\Desktop\\Picture2\\'+np.str(i)+'.jpg',coll[i])
