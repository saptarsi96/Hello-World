# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 10:09:17 2018

@author: sapta
"""

import networkx as nx
import matplotlib.pyplot as plt
G=nx.DiGraph()
waste=list()
value=list()
res=int(input("Enter the target concentration value .. \n"))
val=[float(i) for i in range(0,1025)]
#Populating the array with values
count=0

low=float(input("Enter the buffer concentration value .. \n"))
high=float(input("Enter the sample concentration value .. \n"))
#Setting the buffer and solute sample conc and counter
l=input("Enter the lower bound numbers followed by spaces\n")
lb=list(map(int,l.split()))

h=input("Enter the upper bound numbers followed by spaces\n")
ub=list(map(int,h.split()))


for i in range(0,len(ub)):
    mid=((ub[i]+lb[i])/2)
    value.append(mid)
    count=count+1
    w=input("Enter the weight of the graph \t")
    G.add_edge(ub[i],mid,weight=w,color='b')
    G.add_edge(lb[i],mid,weight=w,color='g')
    
      
    print("The target is",mid,"in",count,"number of steps \n")

p=G.nodes()
c=0
count=1

for i in p:
    if((G.out_degree(i)-G.in_degree(i))%2!=0 and  (-(G.in_degree(i))and G.out_degree(i))):
        print("Waste found at position",i)
        waste.append(i)
        for i in range(0,len(value)):
            if(value[i]==waste[0]):
                index=i
                steps=10-(index+1)
                
        e=int(input("Enter the percentage of error: \t"))
        e1=1+e/100
        e2=1-e/100
        w1=list(G.successors(waste[0]))
        while(w1!=res):
             e1=(e1+1)/2
             e2=(e2+1)/2
             count=count+1
             print("Step",count,"\n")
             print("Positive Error \t",e1)
             print("Negative Error \t",e2)
             c=c+1
             if(c==steps):
                 break