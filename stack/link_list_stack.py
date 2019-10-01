#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 18:28:57 2019

@author: dhruv
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Link_list():
    def __init__(self,data):
        self.head = None
        node = Node(data)
        self.head = node
        
    def push(self,data):
        node=  Node(data)
        node.next = self.head
        self.head = node
    
    def pop(self):
        self.head = self.head.next
    
    def peek(self):
        print(self.head.data)     
    
    def is_empty(self):
        if self.head == None:
            print('empty')
        else:
            print('not empty')
            
    def display(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
            


Link = Link_list(1)
Link.push(2)
Link.display()


Link.pop()
Link.peek()
        
Link.is_empty()
