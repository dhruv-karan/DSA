#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:01:55 2019

@author: dhruv
"""


def Insertion(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            flag = 0
            for j in range(len(array)-1):
                if array[i+1] < array[j] and flag==0:
                    array[j] = array[i+1]
                    flag=1
                    pass
                elif flag==1:
                    array[j] = array[j+1]
        else:
            pass


a = [2,3,1]
Insertion(a)
print(a)

                    
            
        