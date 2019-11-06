#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 22:03:41 2019

@author : dhruv
"""

import math
def find(array,num,left,right):
    mid = math.ceil((left+right)/2)
    
    if left==right:
        return array[left]
    elif left > right:
        return 'NO'
    elif num>array[mid]:
        left = mid+1
        return find(array,num,left,right)
    elif array[mid]>num:
        right = mid-1
        return find(array,num,left,right)
    else:
        return 'No'


a = [1,2,3,4,5,6]



find(a,100000,0,5)
