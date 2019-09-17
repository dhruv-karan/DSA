#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 05:56:42 2019

@author: dhruv
"""

import math
def insert(array,index):
    #array.append(num)
    n = index
    root = math.floor(n/2)
    if array[root]<array[n]:
        array[n],array[root] = array[root],array[n]
        insert(array,root)
        


def delete(array,i):
    if len(array)-1 >=2*i:
        root = array[i-1]
        left = array[2*i-1]
        right = array[2*i]
        if left>right and left>root:
            array[2*i-1],array[i-1] = array[i-1],array[2*i-1]
            i = i+1
            delete(array,i)
        elif right>left and right>root:
            array[2*i],array[i-1] = array[i-1],array[2*i]
            i = i+1
            delete(array,i)
        
            
    else:
        pass


def makeHeap(array):
    b = []
    for i in array:
        b.append(i)
        insert(b,len(b)-1)
    return b

def sort(array):
    b = makeHeap(array)
    s =[]
    for i in range(len(b)):
        s.append(b[0])
        b[0] = b[len(b)-1]
        del[b[len(b)-1]]
        delete(b,1)
    return s

a = [70,50,40,45,35,39,16,10,60]
print(sort(a))