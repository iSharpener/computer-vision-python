# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 19:54:42 2018

@author: Xiaopeng
"""

length = input('Please input the length of cipher code:\n')
keyt = dict()
Lengthlist = list()
for i in range(int(length)):
    Lengthlist.append(i+1)
print('Original list:%s'%Lengthlist)
print('--------------------------------------------------------\n')
for i in range(int(length)):
    flag = True
    while flag:
        value = input('Input the current location of original location %d\n'%(i+1))
        try:
            v = int(value)   
        except Exception as e:
            print('Please reenter the location,you have input a wrong number:\n')
            continue
        if v in Lengthlist:
            keyt[i+1] = value
            Lengthlist.remove(v)
            flag = False
        else:
            print('Please reenter the location,There has no such location in the list:\n')
        
    print('list:%s'%Lengthlist)
    print('--------------------------------------------------------\n')
print('The cipher code you have accomplished just now:%s'%keyt)
print('--------------------------------------------------------\n')
password = input('You have accomplished the cipher code,please input the original password:\n')
number = len(password)//int(length)
print(number)
remainder = len(password)%int(length)
print(remainder)
separate = list()
for i  in range(number):
    separate.append(password[i*int(length):(i+1)*int(length)])
if remainder!=0:
    spacenumber = int(length) - remainder
    space = ''
    for j in range(spacenumber):
        space+='~'
    separate.append(password[-remainder:]+space)
print('The separated password list %s'%separate)
currentseparate = list()
for list1 in separate:
   # print(list1)
    string = ''
    for i in range(len(list1)):
       # print(keyt.get(i+1))
        #print(list1[int(keyt.get(i+1))-1])
        string+=list1[int(keyt.get(i+1))-1]
   # print(string)
    currentseparate.append(string)
newpassword = ''
for s in currentseparate:
    newpassword+=s
print('The new password is %s'%newpassword)
print('--------------------------------------------------------\n')
ye = input('input "yes" to get the original password:\n')
if ye == 'yes':
    oppositekeyt = {int(value):str(key) for key,value in keyt.items()}
    print('oppositekeyt:%s'%oppositekeyt)
    old = ''
    for list1 in currentseparate:
      #  print(list1)
        string = ''
        for i in range(len(list1)):
         #   print(oppositekeyt.get(i+1))
            #print(list1[int(keyt.get(i+1))-1])
            string+=list1[int(oppositekeyt.get(i+1))-1]
       # print(string)
        old+=string
    old=old.replace("~","")
    print(old)
    