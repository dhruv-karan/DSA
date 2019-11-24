#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 10:44:36 2019

@author: dhruv
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Graph:
    def __init__(self,size):
        self.arr = [0]*size
    
    def add_node(self,v1,v2):
        if self.arr[v1-1]==0:
            self.arr[v1-1] = Node(v1)
            self.arr[v1-1].next = Node(v2)
        else:
            a = self.arr[v1-1]
            while a.next:
                a  = a.next
            a.next = Node(v2)
    
    def display(self):
        for i in self.arr:
            print('Node:',i.data)
            i = i.next
            while(i !=None):
                print(i.data)
                i = i.next
            
            
g = Graph(5)
g.add_node(1,2)
g.add_node(1,4)
g.add_node(2,1)
g.add_node(2,3)
g.add_node(3,2)
g.add_node(3,4)
g.add_node(3,5)
g.add_node(4,1)
g.add_node(4,5)
g.add_node(5,3)
g.add_node(5,4)




g.display()
