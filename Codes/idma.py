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
    print("The target is",mid,"in",count,"number of steps \n")

    
