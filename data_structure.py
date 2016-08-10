# List
"""
#Write a Python program to sum all the items in a list.

a =[1,1,-2,45]
sum = sum(a)
print sum 


"""

"""
#Write a Python program to multiplies all the items in a list.

b = [5,6,4,7,8,9,10]
mul = 1
for i in b:
    mul = mul * i 
    
print mul

"""

#Write a Python program to get the largest number from a list.
"""

#b = [5,6,4,7,8,9,10]
large= 0
for i in range(1,100):
    if i > large:
        large = i
    
print large
"""

#Write a Python program to get the smallest number from a list.
"""
b = [5,6,4,7,2,9,10]
small= 15
for i in b:
    if i < small:
        small = i
    
print small
"""

#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
"""
a = [ "ravi" ,"ab" ,"c","heloo","bye",'v','ji','helo']


count = 0
for i in a:
    if len(i) >= 2 :
        count += 1
        
               
print count

"""
"""
# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.


a = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

a.sort()

print a
"""

#Write a Python program to remove duplicates from a list.
"""
b = [5,6,4,7,2,9,10,5,6,7,101,11,51,9]
c = []
for i in b:
    if i not in c:
        c.append(i)
print c
    """
"""    
b = [5,6,4,7,2,9,10,5,6,7,101,11,51,9]

b = set(b)


print b 

"""

#Write a Python program to check a list is empty or not
"""

b = []


if b == []:
    print ' empty list'
else:
    print ' Not an empty list'
"""

#Write a Python program to clone or copy a list
"""
b = [5,6,4,7,2,9,10,5,6,7,101,11,51,9]

a = []

for i in b:
    if i not in a:
        a.append(i)
        
print a 

"""

"""
b = [5,6,4,7,2,9,10,5,6,7,101,11,51,9]
a = list(b)

print a
"""

#Write a Python program to find the list of words that are longer than n from a given list of words.

"""
a = [ "ravi" ,"ab" ,"c","heloo","bye",'v','ji','helo']

b = raw_input('enter the string you want to compare:')

c=[]
for i in a:
    if str(len(i)) > str(len(b)):
        c.append(str(i))
        
print c

"""

"""
# Write a Python function that takes two lists and returns True if they have at least one common member.

a = [ "ab" ,"c","heloo","fat","bye",'v','ji','helo']
b = [ "cat" ,"bat" ,"fat","gat",'vat','jat','helog']

def complist(a,b):
    for i in a:
        for j in b:
        
            if i == j:
                return True


print complist(a,b)


"""
#Write a Python program to print a specified list after removing the 0th, 2nd, 4th and 5th elements.
"""
a = [ "ab","cat","heloo","fat","bye",'vat','jit','helo']

a=[x for (i,x) in enumerate(a) if i not in (0,4,5)]

print a

"""
"""
#Write a Python program to generate a 3*4*6 3D array whose each element is *
array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]  

print(array)
"""
















