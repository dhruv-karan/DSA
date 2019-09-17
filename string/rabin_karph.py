#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:22:59 2019

@author: dhruv
"""

class rabin:
    def __init__(self,pattern):
        self.pattern = pattern
        self.hash = sum([ord(i)*3**j for j,i in enumerate(pattern)])
        self.prev_hash = None
        self.prev_array = None
        
        
    def rolling_hash(self,array):
        if self.prev_hash == None:
            self.prev_hash = sum([ord(i)*3**j for j,i in enumerate(array)])
            self.prev_array = array
        else:
            X = self.prev_hash - ord(self.prev_array[0])
            X = X//3
            X = X + ord(array[len(array)-1])*3**(len(pattern)-1)
            self.prev_hash  = X
            self.prev_array = array
            
            
    
    
a = 'acababcdedf'
pattern = 'abc'
r = rabin(pattern)




for i in range(0,len(a)-len(pattern)-1):
    sub  = a[i:i+len(pattern)]
    r.rolling_hash(sub)
    if r.prev_hash == r.hash:
        print('match')
        break