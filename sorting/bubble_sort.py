#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:30:32 2019

@author: dhruv
"""
def bubble(array):
    flag =0
    i=0
    while(flag!=len(array)-1):
        if array[i]>array[i+1]:
            a = array[i]
            array[i] =array[i+1]
            array[i+1] = a
            flag=1
            i+=1
        elif array[i]<array[i+1]:
            flag+=1
            i+=1
        if len(array)-1==i:
            i=0
    
    return array


array = [5,4,3,2,1]
bubble(array)
        