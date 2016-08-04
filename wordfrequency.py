
a = " This is a cat. This is a dog. This was on the table. The table is very long. Cat is a nice pet. Dot is a nice pet"
alist = a.split()

frequency = [] 

for i in alist:
    frequency.append(i,alist.count(i))
    
b = str(zip(alist,frequency))
#c = dict(b)


#b = set(b)


#print a
#print final

#print frequency

print b 


 
