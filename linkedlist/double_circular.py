#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:28:12 2019

@author: dhruv
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.prev =None
        self.next = None
    
class circular:
    def __init__(self):
        self.head = None
        self.length = 1
    def append(self,data):
        new_node = Node(data)
        if self.head==None:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            new_node.next= self.head
            self.head.prev = new_node
        self.display()
        
    def get_node(self,index):
        temp = self.head
        count =1
        while temp:
            if index == count:
                return temp
                break
            else:
                count+=1
                temp=temp.next
        
        
    def push(self,data):
            new_node = Node(data)
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node
            self.head = new_node
            self.display()
            
    def insert_n(self,index,data):
        if index>self.length:
            print('No such index')
            return 
        else:
            node = self.get_node(index)
            new_node = Node(data)
            new_node.prev = node
            new_node.next = node.next
            node.next = new_node
            node.next.prev = new_node
        self.display()
        
    def display(self):
        count =1
        temp = self.head
        while temp:
            print(temp.data)
            
            if temp.next == self.head.prev:
                self.length = count
                break
            temp = temp.next
            count+=1


clink = circular()
clink.append(1)
clink.append(2)
clink.append(3)
clink.append(4)
clink.append(5)
clink.append(6)
clink.push(0)
clink.insert_n(6,5.5)

clink.display()