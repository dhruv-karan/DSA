#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:27:55 2019

@author: dhruv
"""

class stack:
    def __init__(self):
        self.array = []
    
    def push(self,data):
        self.array.append(data)
    
    def display(self):
        for i in self.array[::-1]:
            print(i)
            
    def pop(self):
        try:
            del(self.array[-1])
            self.display()
        except:
            print('empty List')
        
    def peek(self):
        try:
            print(self.array[-1])
        except:
            print('empty List')
    
sta = stack()

sta.push(1)
sta.push(2)
sta.push(4)
sta.push(1)
sta.push(5)
sta.push(7)
sta.push(2)
sta.push(9)
sta.push(11)
sta.display()

sta.pop()

sta.peek()
