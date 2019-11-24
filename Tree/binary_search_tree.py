#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 20:53:56 2019

@author: dhruv
"""

class Tree:
    def __init__(self,data):
        self.data  = data
        self.left = None
        self.right = None


def make_tree():
    print('enter the root node')
    value = int(input())
    if value !=-1:
        queue = []
        node = Tree(value)
        queue.append(node)
        while(len(queue)>0):
            print('enter the left child of node:', queue[0].data)
            value = int(input())
            if value == -1:
                queue = queue[::-1]
                queue.pop()
                queue = queue[::-1]
            else:
                n = queue[0]
                n.left = Tree(value)
                queue.append(n.left)
                print('enter the right child of node:', queue[0].data)
                value = int(input())
                if value == -1:
                    queue = queue[::-1]
                    queue.pop()
                    queue = queue[::-1]
                else:
                    n = queue[0]
                    n.right =Tree( value)
                    queue.append(n.right)
                    queue = queue[::-1]
                    queue.pop()
                    queue = queue[::-1]
    else:print('Tree is empty')
    return node


def search(num,root):
    if root==None:
        return False
    if root.data == num:
        return True
    elif root.data>num:
        return search(num,root.left)
    elif root.data<num:
        return search(num,root.right)
    
        
        
    
    
    
n1 = make_tree()

search(40,n1)