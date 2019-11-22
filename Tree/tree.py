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

def get_largets_data(root):
    if root ==None:
        return -1
    left = get_largets_data(root.left)
    right = get_largets_data(root.right)
    return max(left,right,root.data)
    
def height(root):
    if root==None:
        return 0
    left = height(root.left)
    right = height(root.right)
    lar = max(left,right)
    return 1+lar
        
def no_of_leaf(root):
    if root ==None:
        return 0
    elif root.left == None and root.right==None:
        return 1
    left = no_of_leaf(root.left)
    right = no_of_leaf(root.right)
    return left+right
    

def print_level_k(root,k):
    if root==None:
        return 
    if k==0:
        print(root.data)
        return
    print_level_k(root.left,k-1)
    print_level_k(root.right,k-1)
    
    
def remove_leaf(root):
    if root == None:
        return  None
    if root.left==None and root.right==None:
        return None
    root.left = remove_leaf(root.left)
    root.right = remove_leaf(root.right)
    return root

def is_balanced(root):
    if root == None:
        return True
    lh = height(root.left)
    lr = height(root.right)
    if abs(lh-lr)>1:
        return False
    is_b_l = is_balanced(root.left)
    is_b_r = is_balanced(root.right)
    if is_b_l and is_b_r:
        return True
    else:
        return False

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
                
                
            
    


n1 = make_tree()

#++++++++++++++++++++++++++++++++++++++=======================FUNCTION CALLS==========================================
prenorder_traversal(n1)
postorder_traversal(n1)
Inorder_traversal(n1)
count_node(n1)
get_largets_data(n1)
height(n1)
no_of_leaf(n1)
print_level_k(n1,2)
root = remove_leaf(n1)
prenorder_traversal(root)
is_balanced(n1)



