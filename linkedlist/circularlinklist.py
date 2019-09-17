#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 06:26:21 2019

@author: dhruv
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next =None

class Linklist:
    def __init__(self):
        self.head = None
    def display(self):
        temp = self.head
        while(temp.next!=self.head):
            print(temp.data)
            temp = temp.next
        print(temp.data)
        
        
    def append(self,data):
        new_node= Node(data)
        temp = self.head
        if temp.next is None:
            temp.next = new_node
            new_node.next = self.head
        while temp:
            if temp.next == self.head:
                break
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head
        
    def push(self,data):
        new_node = Node(data)
        temp = self.head
        while temp.next!=self.head:
            temp= temp.next
        temp.next = new_node
        new_node.next = self.head
        self.head = new_node
    
    def insert(self,index,data):
        #code it

node = Node(1)

link = Linklist()

link.head = node

link.append(2)

link.append(3)
link.append(4)
link.append(5)
link.push(0)
link.append(6)
link.display()




