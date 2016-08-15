"""
#create a tuple
tuple = ()
print tuple 
"""

#create a tuple with different data types 
"""
tuple = ('tuple',False,3.2,1,"helo",11,12,13)
print tuple

"""
"""
#create a tuple of one item, notation without parenthesis

tuple = 4
print tuple


"""
"""
#how to get a item of the tuple in Python

a = (1, "e","c","helo",2,"chalo")

b = a[3] 
print b

"""

# how to find the item in tuple or not
"""
a = (1, "e","c","helo",2,"chalo")
n = raw_input("enter the word:")

for i in a:
    if i == n:
        print n
        break
        
    else:
        print "no"
        
"""

#add item in tuple:
"""
a = (1, "e","c","helo",2,"chalo")

a= a +(5,)


print a 


"""
#updating tuple
"""
t = (12,34,56)
t2= ('abc','xyz')

t3= t + t2 

print t3
"""

"""
#updating tuple , first convert the tuple to list and then update then convert back to tuple 
a = ('physics', 'chemistry', 1997, 2000)

b = list(a)
b.append(8)
a = tuple(b)

print a
"""
"""
#slice a tuple 
 
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

                                                                           

_slice = tuplex[3:5]

print _slice

_slice = tuplex[4:]

print _slice

_slice = tuplex [:7]

print _slice
"""
#Find the index of a item of a tuple

a = tuple("hello what are you doing")

print (a)

index = a.index ("w")
print index









