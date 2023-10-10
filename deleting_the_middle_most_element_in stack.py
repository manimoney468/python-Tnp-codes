l=[21,32,45,63,78]
mid=len(l)//2
k=[]
#del l[mid]
#l.remove(l[mid])
#print(l)
midd=l[2]
for i in range(mid):
    k.append(l.pop())
    
l.pop()    #45 vastahdi kadha andi l lo unthadi
print(k)    
print(l)
for i in range(mid):
    print(i)
    l.append(k.pop())
print(l)
