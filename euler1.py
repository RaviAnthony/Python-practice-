a = range(1,1000)
b = []
c = []
e =[]

for i in a:
    if i%3 == 0:
        b.append(i)
    elif i%5 == 0:
        c.append(i)
print b
print c
e = sum(b+c)
print e