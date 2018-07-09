import networkx as nx
import matplotlib.pyplot as plt
G=nx.DiGraph()

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
    count=count+1
    w=input("Enter the weight of the graph \t")
    G.add_edge(ub[i],mid,weight=w,color='b')
    G.add_edge(lb[i],mid,weight=w,color='g')
    
    #FOR GRAPH COLORING
    pos = nx.circular_layout(G)
    edges = G.edges()
    colors = [G[u][v]['color'] for u,v in edges]
    nx.draw(G, pos=pos, edges=edges, edge_color=colors,with_labels=True,width=1,font_family='sans-serif')
    plt.figure()
    plt.show()
    
    #FOR GRAPH COLORING
    
    print("The target is",mid,"in",count,"number of steps \n")

p=G.nodes()
for i in p:
    if((G.out_degree(i)-G.in_degree(i))%2!=0 and  (-(G.in_degree(i))and G.out_degree(i))):
        print("Waste found at position",i)
        e=int(input("Enter the percentage of error: \t"))
        
        e1=1+e/100
        e2=1-e/100
        w1=list(G.successors(i))
        #print(w1)
        w2=list(G.predecessors(w1[0]))
        #print(w2)
        w2.remove(i)
        #print(w2)
        pe=((i*e1)+(w2[0]*1))/(1+e1)
        ne=((i*e2)+(w2[0]*1))/(1+e2)
        
        print("Possitive error:  \t ",pe)
        print("Negative error:   \t",ne)
        
nx.draw_circular(G,with_labels=True)