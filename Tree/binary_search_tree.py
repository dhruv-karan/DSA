#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 20:53:56 2019

@author: dhruv
"""
from queue import Queue 

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
    
def print_range(root,min_,max_):
    if root ==None:
        return
    if root.data >min_ and root.data<max_:
        print(root.data)
    if root.data<min_:
        print_range(root.right,min_,max_)
    elif root.data>max_ :
        print_range(root.left,min_,max_)
    else:
         print_range(root.right,min_,max_)
         print_range(root.left,min_,max_)

      
def arry2bst(arr):
    middle = int(len(arr)/2)
    if len(arr) ==0:
        return
    node = Tree(arr[middle])
    node.left = arry2bst(arr[:middle])
    node.right = arry2bst(arr[middle+1:])
    return node

def min_(root):
    if root == None:
        return 10000
    left = min_(root.left)
    right = min_(root.right)
    mi = min(left,right,root.data)
    return mi

def max_(root):
    if root == None:
        return -1
    left = min_(root.left)
    right = min_(root.right)
    mx = max(left,right,root.data)
    return mx



def levelwise_traversal(root):
    q = Queue()
    q.put(root)
    while(True != q.empty()):
        root = q.get()
        if root == None:
            q.get()
        else:
            print(root.data)
            q.put(root.left)
            q.put(root.right)
            




    
n1 = make_tree()
search(40,n1)
print_range(n1,4,15)
node = arry2bst([1,2,3,4,5,6,7])
levelwise_traversal(n1)


min_(n1)
max_(n1)





