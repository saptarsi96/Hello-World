# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 07:49:45 2018

@author: sapta
"""

import networkx as nx
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import matplotlib.pyplot as plt

G=nx.DiGraph()

res=int(input("Enter the target concentration value .. \n"))
val=[float(i) for i in range(0,1025)]
#Populating the array with values
count=0
low=float(input("Enter the buffer concentration value .. \n"))
high=float(input("Enter the sample concentration value .. \n"))
#Setting the buffer and solute sample conc and counter
l=int(input("Enter the lower bound numbers followed by spaces\n"))
lb=list(map(int,l.split()))

h=int(input("Enter the upper bound numbers followed by spaces\n"))
ub=list(map(int,h.split()))


for i in range(0,len(ub)):
    mid=((ub[i]+lb[i])/2)
    
    count=count+1
    w=input("Enter the weight of the graph \t")
    G.add_edge(ub[i],mid,weight=w,color='b')
    G.add_edge(lb[i],mid,weight=w,color='g')
    

    
print("The target is",mid,"in",count,"number of steps \n")
