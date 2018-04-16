# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 09:13:52 2018

@author: Xiaopeng
"""
length = input('Please input the length of the cipher code:\n')
keyt = list()
for i in range(int(length)):
    flag = True
    while flag:
        key = input('Please input the key value of location %d\n'%i)
        try:
            if int(key)>25 or int(key)<0:
                print('Please input the number between 0 and 25!')
                continue
            keyt.append(int(key))
            flag = False
        except:
            print('You hava input a wrong key number,please reenter it:\n')
            continue
    print('------------------------------------------------------------')
print('The cipher code is %s'%keyt)
password = input('Please input the original password:\n')
password = password.replace(' ','')
#asclist = [ascll(c) for c in password]
print('------------------------------------------------------------')
separate = list()
number = len(password)//int(length)
remainder = len(password)%int(length)
for i in range(number):
    separate.append(password[i*int(length):(i+1)*int(length)])
if remainder!=0:
    separate.append(password[-remainder:])
print(separate)
newpassword = ''
newpswlist = list()
for item in separate:
    print(item)
    for i in range(len(item)):
        s = (ord(item[i])-97+keyt[i])%26+97
        newpassword+=chr(s)
print('The new password is %s'%str.upper(newpassword))
