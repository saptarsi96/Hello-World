n=int(input("Enter the target concentration value .. \n"))
val=[float(i) for i in range(0,1025)]
#Populating the array with values
count=0
low=float(input("Enter the buffer concentration value .. \n"))
high=float(input("Enter the sample concentration value .. \n"))
#Setting the buffer and solute sample conc and counter

while(low<=high):


    mid=float((low+high)/2.0)
    mid=round(mid,1)
    
    count=count+1
    for i in range(1,count):
        #mid=pe[i]
        #print("High:\t",high,"Low:\t",low,"Target:\t",mid,"Steps:\t",count,)
        print("High:\t",high,"Low:\t",low,"Target:\t",mid,"Steps:\t",count,)
    
    
    if n==mid:
        print("Found at position",mid,"in",count,"steps")
        break
    elif mid>n:
        high=mid
    else:
        low=mid
    


#Finding the number of steps in which we can attain the desired target concentration

