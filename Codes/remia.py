import networkx as nx
import matplotlib.pyplot as plt

target=int(input("Enter the target concentration \t"))
G=nx.DiGraph()
power_val=list()
sample=list()
for i in range(0,11):
    power_val.append(pow(2,i))
for i in range(0,6):
    for i in range(0,len(power_val)):
        if power_val[i]>=target:
            y=power_val[i]
            print("The lower side is \t",y)
            break
            
            
    x=target*2-y
    
    G.add_edge(y,target)
    G.add_edge(x,target)
    print("The upper side is \t",x)
    target=x
    
    
    if(x%pow(2,i)==0):
        break
nx.draw_circular(G,with_labels=True)

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