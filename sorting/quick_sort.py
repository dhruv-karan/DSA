#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 19:14:33 2019

@author: dhruv
"""

"""
=============================================sorting with end pivot===============================================


def partion(array,low,high):
    i = (low-1)
    pivot = array[high]

    for j in range(low,high):
        if pivot>array[j]:
            i=i+1
            array[i],array[j] = array[j],array[i]
        
    
    array[i+1],array[high] = array[high],array[i+1]
    return (i+1)

def quick(array,low,high):
    if high>low:
        
        pi = partion(array,low,high)
        quick(array,low,pi-1)
        quick(array,pi+1,high)
    


a = [10,7,8,9,1,5,2] [2,7,8,9,1,5,10]

[1,2,8,9,10,5,7]
[1,2,5,9,10,8,7]
[1,2,5,7,8,9,10]


quick(a,0,6)

"""



def partion(array,low,high):
    i = (low-1)
    pivot = array[low]
    
    for j in range(low,high):
        if pivot>array[j]:
            i=i+1
            array[i],array[j] = array[j],array[i]
        
    
    array[i+1],array[high] = array[high],array[i+1]
    return (i+1)

def quick(array,low,high):
    if high>low:
        
        pi = partion(array,low,high)
        quick(array,low,pi-1)
        quick(array,pi+1,high)
    


a = [10,7,8,9,1,5,2]

quick(a,0,6)




