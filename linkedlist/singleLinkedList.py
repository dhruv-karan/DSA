#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 08:37:02 2019

@author: dhruv
"""


class Node:
    def __init__(self,data):
        self.data =  data
        self.next = None


class linkedList:
    def __init__(self,node):
        self.head =node
        
    def display(self):
        temp= self.head
        while temp:
            print(temp.data)
            temp = temp.next
            
    def push(self,data):
        new_node= Node(data)
        
        new_node.next = self.head
        self.head = new_node
    
    def insertn(self,prev_node,data):
        new_node = Node(data)
        if prev_node is None:
            print('Node does not exist')
            return 
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def insertend(self,data):
        new_node = Node(data)
        if self.head is None:
            print('emplty List')
            return
        last = self.head
        while last.next:
            last = last.next
            
        last.next = new_node
    
    def delete_index(self,number):
        if self.head is None:
            print('empty List')
            return
        index =1
        last = self.head
        while last.next and index!=number:
            last = last.next
            index+=1
        if last.next is None:
            print('dhd',index)
            return
        elif number==1:
            self.head = last.next
            self.display()
            return
        last.next = last.next.next
        self.display()
        
    def length(self):
        count = 1
        temp = self.head
        while temp.next:
            temp = temp.next
            count = count+1
        print(count)
    
    def search_ele(self,num):
        temp = self.head
        while temp.next:
            temp = temp.next
            if temp.data==num:
                print('found')
                return
            
    def get_node(self,num):
        index=1
        temp = self.head
        while temp.next and index!=num:
            temp = temp.next
            index+=1
        return temp
    
    def rotateList(self, k):
        head = self.head
        temp = head
        current = head
        last = None
        while temp:
            if temp.next is None:
                last = temp  
            temp = temp.next
        while k>1:
            head = current.next
            current.next = None
            last.next = current
            current = head
            last = last.next
            k = k-1

        

one =  Node(1)
link = linkedList(one)
two = Node(3)
three = Node(2)
four = Node(10)
five = Node(5)
six = Node(6)


link.head.next = two

two.next = three
three.next = four
four.next = five
five.next = six
link.push(7)
link.display()


link.rotateList(2)

link.display()









link.insertn(five,5.5)
link.insertend(9)
link.display()
link.length()
link.search_ele(9)

a = link.get_node(1)
a.data




#link.delete_index(1)