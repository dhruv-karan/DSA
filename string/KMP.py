#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 07:34:53 2019

@author: dhruv
"""




a = 'abcabc'

ls = [] 
i=j=0
while(i<len(a)):
    if i==0 and j==0:
        ls.append(0)
        i = i+1
    elif a[i]==a[j]:
        ls.append(j+1)
        i = i+1
        j =j+1
    elif a[i]!=a[j] and j==0:
        ls.append(0)
        i = i+1
    elif a[i]!=a[j] and j!=0:
        j = ls[j-1]



text = 'abxabcabyaby'
l =p=0

while (p<len(text)):
    if a[l] == text[p]:
        l = l+1
        p = p+1
    elif a[l]!=text[p] and l!=0:
        l = ls[l-1]
    elif a[l] !=text[p] and l==0:
        p =  p+1
    if l== len(ls) and a[l-1] == text[p-1]:
        print('pattern found')
        break
        

        