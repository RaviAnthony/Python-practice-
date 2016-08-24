"""
a = " This is a cat. This is a dog. This was on the table. The table is very long. Cat is a nice pet. Dot is a nice pet"
alist = a.split()

d = []
frequency = [] 

for i in alist:
    frequency.append(i)
    d.count(i)
    
b = str(zip(d,frequency))
#c = dict(b)


#b = set(b)


#print a
#print final

#print frequency

print b

"""

a = " This is a cat. This is a dog. This was on the table. The table is very long. Cat is a nice pet. Dot is a nice pet"
a = a.split()
#print alist
b =[]
d = {}

for i in a:
    c = a.count(i)
    b.append((i,c))

dict_ = dict(b)

print dict_

 

"""
sentence = '" This is a cat. This is a dog. This was on the table. The table is very long. Cat is a nice pet. Dot is a nice pet"'.split()
ls = []  
for i in sentence:

    word_count = sentence.count(i)  # Pythons count function, count()
    ls.append((i,word_count))       


dict_ = dict(ls)

print dict_        



"""



