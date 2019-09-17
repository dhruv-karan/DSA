#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:20:21 2019

@author: dhruv
"""

class Graph:
    graph = {}
    def add_note(self,node,ni):
        if node not in self.graph:
            self.graph[node] = [ni]
        else:
            self.graph[node].append(ni)
    
    def show(self):
        for i in self.graph:
            for j in self.graph[i]:
                print(i,j)
    
    def find_path(self,start,end,path=[]):
        path = path+[start]
        if start==end:
            return path
        for i in self.graph[start]:
            if i not in path:
                newPath =  self.find_path(i,end,path)
                if newPath:
                    return newPath
                else:
                    return None
        


g1 = Graph()

g1.add_note('1','2')
g1.add_note('1','3')
g1.add_note('2','3')
g1.add_note('3','2')
g1.add_note('4','1')
g1.show()

