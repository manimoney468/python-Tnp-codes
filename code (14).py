l=[12,14,2,3,4,20]
res=[]
k="-1"
for i in range((len(l)+1)):
    ele=l[i]
    count=0
    for m in range((i+1),(len(l)+1):
        bal=len(l)-(i+1)
        count+=1
        if (ele<l[m]):
            res.append(l[m])
            break
        elif count==bal:
            res.append(k)
            break
    count=0




print(res) 


"""



l = [12, 14, 2, 3, 4, 20]
res = []
k = "-1"
for i in range(len(l)):
    ele = l[i]
    count = 0
    for m in range(i + 1, len(l)):
        bal = len(l) - (i + 1)
        count += 1
        if ele < l[m]:
            res.append(l[m])
            break
        elif count == bal:
            res.append(k)
            break
    count = 0

print(res)


"""
