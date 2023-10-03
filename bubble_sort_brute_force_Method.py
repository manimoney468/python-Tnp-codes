in_arr=[2,3,34,5,67,8,9]


for i in range(len(in_arr)-1):#this -1 is for the i=0=n-i-1 no need to search first element with it self
    for j in range(0,(len(in_arr)-i-1)):
        if(in_arr[j]>in_arr[j+1]):
            temp=in_arr[j]
            in_arr[j]=in_arr[j+1]
            in_arr[j+1]=temp
            
            
            
print(in_arr)            
