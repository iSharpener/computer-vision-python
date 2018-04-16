# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 17:39:25 2018

@author: Xiaopeng
"""
import matplotlib.pyplot as plt
from skimage import io
import cv2
def contra(c,i):
    img = cv2.imread(i)
    img = img*1.0
    thre = img.mean()
    contrast = c
    img_out = img*1.0
    if contrast<=-255.0:
        img_out = (img_out>=0)+thre-1
    elif contrast >-255.0 and contrast<0:
        img_out = img + (img-thre) * contrast /255.0
    elif contrast >=0 and contrast < 255.0:
        new_con = 255.0 * 255.0/(256.0-contrast)-255.0
        img_out = img+(img-thre) * new_con /255.0
    else:
        mask_1 = img>thre
        img_out = mask_1 *255
    img_out = img_out / 255.0
 #   print(img_out)
    mask_1 = img_out < 0
    mask_2 = img_out > 1
    img_out = img_out *(1-mask_1)
    img_out = img_out *(1-mask_2)+mask_2
    cv2.imshow('original picture',img/255.0)
    
    cv2.imshow('Changed picture',img_out)
    keycode = cv2.waitKey(0)
    if keycode == 0:
        cv2.imshow('Change picture',img)
    #cv2.destroyAllWindows()
    if keycode == 23:
        cv2.destroyAllWindows()
contrast = input('请输入对比度的值')
contra(float(contrast),'C:\\Users\\Xiaopeng\\Desktop\\Picture\\coffee.jpg')    