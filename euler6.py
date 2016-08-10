
b =[]
for i in range(1,101):
    a=i**2
    b.append(a)  
print b 
c= sum(b)
print c
d = []
for i in range(1,101):
    if i not in d:
        d.append(i)
print d 
e = sum(d)
f = e**2
print f

g = f - c

print g 