
"""
#Write a Python program to create a tuple.

a = ()

print a 

"""

#Write a Python program to create a tuple with different data types.
"""
a = ("ravi",4,"kavi",5,"savi",6)

print a 


"""
"""
#Write a Python program to create a tuple with numbers and print one item.


a = (1,2,3,4,5,6)

index = a[3]

d = a[1:4]

print index
print d
"""

"""
#Write a Python program to unpack a tuple in several variables

a = (1,2,3,)

n1,n2,n3 =  a 
print(n1+n2+n3)

"""
#Write a Python program to add an item in a tuple.
"""
a = (1,2,3,4,5,6)

b = list(a)
b.append(8)
print b 
a = tuple(b)
print a 

"""
"""
#Write a Python program to convert a tuple to a string

a = ("s","d","f","g","h","t","r","e")
b = ''.join(a)

print b 
"""
"""
#Write a Python program to get the 4th element and 4th element from last of a tuple

a = (1,2,3,4,5,6,7,8,9,10,11,12)
b = len(a)
print b 

e = a[3]
f = a[b-4]
print e
print f

"""
"""
#Write a Python program to create the colon of a tuple.

from copy import deepcopy

a = ("ravi",4,"kavi",5,"savi",6) 
print a 
b = deepcopy(a)
#b[2].append(30)
print b 

"""
"""
#Write a Python program to find the repeated items of a tuple

a = ("ravi",4,"kavi",5,"savi",6,"savi",4,5,"kavi") 

b = a.count(4)

print b 

"""
"""
#Write a Python program to check whether an element exists within a tuple

a = ("ravi",4,"kavi",5,"savi",6,"savi",4,5,"kavi")

b = int (input("enter the number : "))

for i in a :
    if i == b :
        print "yes"
        break
   
    
    
""" 
   
"""
#Write a Python program to convert a list to a tuple

a = (1,2,3,4,5,6,7,8,9,10,11,12)

b = list(a)

print b

a = tuple(b)

print a 

"""
"""
#Write a Python program to remove an item from a tuple.


a = (1,2,3,4,5,6,7,8,9,10,11,12)

b = list(a)
print b 

del b[2]

a = tuple(b)
print a 
"""
"""
#Write a Python program to slice a tuple

a = (1,2,3,4,5,6,7,8,9,10,11,12)

_slice = a[2:5]

print _slice


"""

"""
#Write a Python program to find the index of a item of a tuple
a = (1,2,3,4,5,6,7,8,9,10,11,12)
index= a.index(3)
print index
"""
"""
#Write a Python program to find the length of a tuple.

a = (1,2,3,4,5,6,7,8,9,10,11,12)

b = len(a)

print b 
"""
"""
#Write a Python program to convert a tuple to a dictionary

a = ((2,"w"),(3,"r"))


#print (dict((y,x) for x,y in a))

"""

"""
#Write a Python program to unzip a list of tuples into individual lists.

l = [(1,2), (3,4), (8,9)]
print(list(zip(*l)))

"""
"""
#Write a Python program to reverse a tuple

a = (1,2,3,4,5,6,7,8,9,10,11,12)

b = list(a)

b.reverse()
print b

a = tuple(b)
print a 

"""
"""
#Write a Python program to convert a list of tuples into a dictionary.

l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)] 

d={}

for a, b in l:
    d.setdefault(a,[]).append(b)
    
print (d)

"""


























