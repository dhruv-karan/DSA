#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 07:26:48 2019

@author: dhruv
"""

class Queue:
    def __init__(self):
        self.array = []
    
    def enque(self,data):
        self.array.append(data)
    
    def deque(self):
        del(self.array[0])
    
    def display(self):
        print('from front to rear')
        print(self.array)


que = Queue()
que.enque(1)
que.enque(2)
que.enque(3)
que.enque(4)
que.enque(5)
que.enque(6)
que.enque(7)
que.enque(8)

que.display()

que.deque()
que.display()
