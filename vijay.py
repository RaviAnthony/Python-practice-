"""a =[1,1,1,1,2,3,4,5,4,4,4,4,3,4,5]

b = []
#a.sort()
for i in a:
    if i not in b:
        b.append(i)
print b """
    
a=[1,1,1,1,1,1,1,1,2,3,4,5,4,4,4,4,3,4,5]
b=[]
for i in a:
    if i not in b:
        b.append(i)
        c = a.count(i)
        print i , c
   