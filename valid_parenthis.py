inpu="(()[(})])"

k=[]


for i in range(len(inpu)):
    if inpu[i]=='(':
        k.append(inpu[i])
    elif inpu[i]=='{':
         k.append(inpu[i])
    elif inpu[i]=='[':
         k.append(inpu[i])
    elif inpu[i]==')' and k[-1]=='(':
         k.pop() 
    elif inpu[i]=='}' and k[-1]=='{':
         k.pop()         
    elif inpu[i]==']'and k[-1]=='[':
         k.pop()     
    else:
        k.append(inpu[i])
             
print(k)
if(len(k)==0):
    print('yes')
else:
    print("no")
