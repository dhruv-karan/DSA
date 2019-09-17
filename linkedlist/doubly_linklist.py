#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:33:25 2019

@author: dhruv
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
        

class linklist:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if new_node.next is not None:
            new_node.next.prev = new_node
    
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            
    def length(self):
        count = 1
        temp = self.head
        while temp.next:
            temp = temp.next
            count +=1
        return count
    
    
    def getnode(self,index):
        if index > self.length():
            print('No such exits')
            return
        num = 1
        temp = self.head
        while temp:
            if num==index:
                return temp
            temp = temp.next
            num +=1
    
            
    def insert(self,data,index):
        if index==1:
            self.push(data)
        else:
            node = self.getnode(index)
            new_node = Node(data)
            new_node.prev = node
            new_node.next = node.next
            node.next = new_node
            if new_node.next is not None:
                new_node.next.prev = new_node
        self.display()
    
    def delete(self,index):
        node = self.getnode(index)
        node.prev.next = node.next
        node.next.prev = node.prev

link = linklist()

node = Node(1)
link.head = node


link.push(2)
link.push(3)
link.push(4)
#link.display()
link.length()
link.insert(5,1)

link.delete(3)

link.display()

