# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 18:43:27 2018

@author: Xiaopeng
"""

from skimage import io,color,data_dir
import matplotlib.pyplot as plt


def contra(c,i):
    img = io.imread(i)
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
    
    plt.figure()
    plt.title('a')
    plt.imshow(img/255.0)
    plt.axis('off')

    plt.figure(2)
    plt.title('b Change the contract of "a" to %f'%c)
    plt.imshow(img_out)
    plt.axis('off')
def light(l,i):
    img = io.imread(i)
    hsv= color.rgb2hsv(img)
    hsv = hsv*1.0
    #转换为0-1的float类型
    new_img = img/255.0
    rows,cols,dim = img.shape
    if l >1:
        l=1
    if l<0:
        l=0
    for i in range(rows):
        for j in range(cols):
            if l>=0.5:
                new_img[i,j,2]+=(1-new_img[i,j,2])*(l-0.5)/0.5
                new_img[i,j,0]+=(1-new_img[i,j,0])*(l-0.5)/0.5
                new_img[i,j,1]+=(1-new_img[i,j,1])*(l-0.5)/0.5     
            else:
                new_img[i,j,2]=new_img[i,j,2]*l/0.5
                new_img[i,j,1]=new_img[i,j,1]*l/0.5
                new_img[i,j,0]=new_img[i,j,0]*l/0.5
   # new_img = color.hsv2rgb(hsv)    
   
    #print(new_img)
    plt.figure(3)
    plt.title('a'+'')
    plt.imshow(img)
    plt.axis('off')

    plt.figure(4)
    plt.title('b Change the lightness of "a" to %f'%l)
    plt.imshow(new_img)
    plt.axis('off')
def satura(s,i):
    img = io.imread(i)
    hsv = color.rgb2hsv(img)
    rows,cols,dim = hsv.shape
    if s >1:
        s=1
    if s<0:
        s=0
    for i in range(rows):
        for j in range(cols):
            if s>=0.5:
                hsv[i,j,1]+=(1-hsv[i,j,1])*(s-0.5)/0.5
            else:
                hsv[i,j,1]=hsv[i,j,1]*s/0.5
    new_img = color.hsv2rgb(hsv)    
    plt.figure(5)
    plt.title('a'+'')
    plt.imshow(img)
    plt.axis('off')

    plt.figure(6)
    plt.title('b Change the satura of "a" to %f'%s)
    plt.imshow(new_img)
    plt.axis('off')
    
while True:   
    choice = input('Please choose the option\'s number you need see the changed p'
       +'icture:\n1.Change the contrast.\n2.Change the lightness.\n3.Change the saturation.'
       +'\n4.Exit.\n')
    if choice =='1':    
        print('Contrast...\n')
        size = input('Input the contrast:\n')
        contra(float(size),'C:\\Users\\Xiaopeng\\Desktop\\Picture\\coffee.jpg')
    elif choice == '2':
        print('Lightness...\n')
        size = input('Input the lightness:\n')
        light(float(size),'C:\\Users\\Xiaopeng\\Desktop\\Picture\\coffee.jpg')
       # light(float(size),data_dir+'\\chelsea.png')
    elif choice == '3':
        print('Saturation...')
        size = input('Input the saturation:\n')
        satura(float(size),'C:\\Users\\Xiaopeng\\Desktop\\Picture\\coffee.jpg')
      # satura(float(size),data_dir+'\\chelsea.png')
    elif choice =='4':
        break
