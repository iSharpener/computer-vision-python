# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 08:40:43 2018

@author: Xiaopeng
"""

from PIL import Image
from PIL import ImageEnhance
from skimage import data_dir
#导入原始图像
image = Image.open(data_dir+'\\coffee.png')
image.show()
image2 = image
while True:
    lightness = input('请输入亮度:')
    en_hance = ImageEnhance.Brightness(image2)
    brightness = 1.5
    image2 = en_hance.enhance(brightness)
    image2.show()
    if lightness == 'q':
        break