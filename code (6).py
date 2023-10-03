in_arr=[2,3,34,5,67,8,9]
in_arr.sort()
print(in_arr)
l=0
h=len(in_arr)-1
mid=l+h//2
print(mid)
ele=68
while(l<=h):
    if(in_arr[mid]==ele):
        print(mid)
        print("ssucess",in_arr[mid])
        break
    elif(ele<in_arr[mid]):
        h=mid-1
    elif(ele>in_arr[mid]):
        l=mid+1
    mid = (l + h) // 2    
    
else:
    print("not found sir")
    