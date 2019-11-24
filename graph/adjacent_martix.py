#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 09:02:23 2019

@author: dhruv                                        
"""

class Graph:
    def __init__(self,size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size
    
    def addEdge(self,v1,v2):
        if v1==v2: print('Same')
        self.adjMatrix[v1-1][v2-1] = 1
        self.adjMatrix[v2-1][v1-1] = 1
        
    def display(self):
        print(self.adjMatrix)
        

g1 = Graph(3)
g1.addEdge(1,2)
g1.addEdge(1,3)
g1.addEdge(2,1)
g1.addEdge(2,3)
g1.addEdge(3,1)
g1.addEdge(3,2)


g1.display()
