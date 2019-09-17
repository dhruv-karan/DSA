#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 05:45:53 2019

@author: dhruv
"""

def Merge(L,R,arr):
    i=j=k=0
    while len(L)>i and len(R)>j:
        if L[i]<R[j]:
            arr[k] = L[i]
            i+=1
        elif L[i]>R[j]:
            arr[k] = R[j]
            j+=1
        k+=1
    
    while len(L)>i:
        arr[k] = L[i]
        k+=1
        i+=1
    while len(R)>j:
        arr[k] =R[j]
        k+=1
        j+=1
    
    
def Mergesort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        L = arr[mid:]
        R = arr[:mid]
        
        Mergesort(L)
        Mergesort(R)
        Merge(L,R,arr)
    

a=[1,3,4,2,5,9,0]
Mergesort(a)