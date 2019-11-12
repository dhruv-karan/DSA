#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:12:10 2019

@author: dhruv
"""

class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
        
def prenorder_traversal(root):# This is preorder traversal
    if root==None:
        return
    print(root.data)
    prenorder_traversal(root.left)
    prenorder_traversal(root.right)

def postorder_traversal(root):# This is postorder traversal
    if root==None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data)

def Inorder_traversal(root):# This is postorder traversal
    if root==None:
        return
    Inorder_traversal(root.left)
    print(root.data)
    Inorder_traversal(root.right)

def count_node(root):
    if root == None:
        return 0
    left = count_node(root.left)
    right = count_node(root.right)
    return 1+left+right


        
n1 = Tree(1)
n2 = Tree(2)
n3 = Tree(3)
n4 = Tree(4)
n5 = Tree(5)
n6 = Tree(6)
n7 = Tree(7)



n1.left= n2
n1.right=n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7


prenorder_traversal(n1)
postorder_traversal(n1)
Inorder_traversal(n1)


count_node(n1)

 
