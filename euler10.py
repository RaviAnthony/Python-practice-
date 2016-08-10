"""
b =[]
for num in range(2,200000):
   # prime numbers are greater than 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
               break
            else:
                #print (num)
                b.append(num)
#print b
c= sum(b)
print c """

import math 
b =[]
for num in range(2,2000000):
   # prime numbers are greater than 1
    if num > 1:
        for i in range(2,int(math.sqrt(num)+1)):
            if (num % i) == 0:
               break
            else:
           #print (num)
                    b.append(num)
#print b
c= sum(b)
print c
