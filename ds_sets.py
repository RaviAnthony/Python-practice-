"""
#create a set in python
a = set()
print a 

# A non empty set 

n = set ([0,1,2,3,4,5])
print (n)
"""
"""
#iteration oversets

num_set = set ([0,1,2,3,4,5])

for n in num_set:
    print (n)

"""
"""
#add member(s) in Python set 

c = set ()
c.add("ravi")

print c 

c. update(["blue","Green","yellow","fellow"])
print c
"""
"""
#Remove item(s) from Python set

n = set ([0,1,2,3,4,5])

n.pop()

print n 
n.discard(5)
print n 
n.remove(3)
print n 
"""
"""
#Intersection of sets
n = set ([0,1,2,3,4,5])

b =  set ([0,1,2,5])

d = n & b 

print d 
"""
"""
#Union of sets

n = set ([0,1,2,3,4,5])

b =  set ([0,1,2,5])

d = n | b 

print d 
"""
"""
#Set difference

n = set ([0,1,2,3,4,5])
b =  set ([0,1,2,5,6])
d = n - b 

print d 

"""
"""
# Symmetric difference
n = set ([0,1,2,3,4,5])
b =  set ([0,1,2,5,6])
d = n ^ b 
print d 
"""
"""
#issubset and issuperset

n = set ([0,1,2,3,4,5])
b =  set ([0,1,2,5,6])
d =  n <= b 
print d 
c =  n >= b 
print c  

"""
"""
#Shallow copy of sets

n = set ([0,1,2,3,4,5])
b =  set ([0,1,2,5,6])

c = b.copy() 

print c  

#Clear sets

n = set ([0,1,2,3,4,5])


c = b.copy() 
c. clear()
print c 

"""


"""
#Remove item(s) from Python set

n = set ([0,1,2,3,4,5])

n.pop() #pop() take no arruguments

print n
"""
"""
 #Write a Python program to find the length of a set.
 
n = set ([0,1,2,3,4,5])

print len(n)


"""
#Write a Python program to find maximum and minimum value in a set.

n = set ([0,1,2,3,4,5])

print max(n)
print min(n)















