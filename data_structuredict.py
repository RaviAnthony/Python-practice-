#Create the Dictionary 
"""
a= {1:23,3:45,4:55,5:66,'d':'helo'}

print a 

print a[1]
print a['d']

a['b']= ' what '
a['c']= ' wat '

print a

for i in a: 
     if 'b' in a:
        del a['b']
        
print a
    
"""


#Write a Python script to sort (ascending and descending) a dictionary by value.


"""
a={5:53,6:64,7:74,8:67}
sorted(a.value())

print a 




"""

"""
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
            
        else:
            d[c] +=1
            
    return d 

print histogram("gowraaaaaaaaaaaaaaaaatulips")



"""

#reverse look update
"""
def reverse_lookup(d,v):
    for k in d:
        if d[k]== v:
            return k
            
            
            
            
            
b = 'heloo'
print reverse_lookup(b,2 )
      

"""


"""
known = {0:0,1:1}

def fibonacci(n):
    if n in known:
        return known[n]
        
    res = fibonacci(n-1)+ fibonacci(n-2)
    known[n] = res 
    return res 
    
    
print fibonacci(11)    
   """

"""
#descending a dictionary
#if you want to find the descending order you have to rever
a={5:53,6:64,7:74,8:67}

view =reversed(sorted(a))

for a in view:
    print (a)
    
    """
"""    
a={5:53,6:64,7:74,8:67}

reversed(sorted(a))

print a
"""
"""
a={5:53,11:64,2:74,8:67}
view =reversed(sorted(a))

for a in view:
    print a
   
   """
   
   
#Write a Python script to add key to a dictionary.
""""
a={5:53,11:64,2:74,8:67}


a.update({10:88})

print a


"""

#Write a Python script to concatenate following dictionaries to create a new one
"""
a={1:10, 2:20}
b={3:30, 4:40}
c={5:50,6:60}

d={}

for d in(a,b,c):
    d.update(d)
    print d

"""

#Write a Python script to check if a given key already exists in a dictionary.
"""
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
x = int(input("enter the number :"))

#def is_key_present(x):
if x in d:
    print('Key is present in the dictionary')
else:
    print('Key is not present in the dictionary')
      
#is_key_present(3)

"""
#Write a Python program to iterate over dictionaries using for loops.
"""

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

for dict_key in d.items():  
    print(dict_key,'->',dict_value) 
    
    """


#Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included)

"""
d ={}

n = int(input("enter the number:"))
for i in range(1,n+1):
    d[i]= i*i
    
print d
"""

"""




if d not in b:
     b.update(d)
print b

"""
"""
#del
a={1:10, 2:20}

if 1 in a:
    del a[1]
    
    
print a    
"""

"""
d = {'ashik':27,'dheeraj':25,'raghu':28}

if 'ashik' in d:
    del d['ashik']
    
print d

"""
"""
#Write a Python script to merge two Python dictionaries

a={1:10, 2:20}
b={3:30, 4:40}

c = b.copy()
c.update(a)
print(c)
"""
"""
#Write a Python program to iterate over dictionaries using for loops.
d = {'ashik':27,'dheeraj':25,'raghu':28,'hanu':25,'helo':26}

for name_key,value in d.items():
    print(name_key,'corresponds',d[name_key])
    
    
    
"""

"""
#Write a Python program to sum all the items in a dictionary


a={1:10, 2:20}

sum= sum(a.values())

print sum 

"""
#Write a Python program to multiply all the items in a dictionary
"""
a={1:10, 2:20,3:30, 4:40}

res=1
for key in a:
    res=res*a[key]
print res

"""
#Write a Python program to remove a key from a dictionary.
"""
a={1:10, 2:20,3:30, 4:40}


if 2 in a:
    del a[2]
    
print a


"""
#Write a Python program to map two lists into a dictionary.
"""
a=['ravi','kavi','pavi','savi','tovi']
b=['sui','pui','kui','hui','lui']

c = dict(zip(a,b))

print c 

#zip(key,values) method is used to map the two values in dictionary.

"""

#Write a Python program to sort a dictionary by key.
"""
a={1:10, 2:20,7:30, 3:40,5:30,4:20}

sorted(a)

print a 

"""

#Write a Python program to get the maximum and minimum value in a dictionary.
"""
a={1:10, 2:20,7:30, 3:40,5:30,4:20}

max=max(a.values())
print max

min = min(a.values())

print min

"""
#Write a Python program to get a dictionary from an object's fields.

#Write a Python program to remove duplicates from Dictionary
"""
*******
helo = {'a':{1:10, 2:20,7:30, 3:40,5:30,4:20},'b':{1:10, 2:20,3:30, 4:40} }
final={}
for key,value in helo.items():
    if value not in final.values():
        final[key]= value
        
print final
"""
#Write a Python program to check a dictionary is empty or not

a ={}
if a:
    print" non empty"
else:
    print" empty"



