'''number = 23 
guess = int(input('enter the integer: '))
if guess == number :
    print("you guess is correct")
    
elif guess > number:
    print(" you guess is higher than the actual number")
    
else: 
    print('you guess is less than the actual number')
    

'''
'''
a = raw_input(" enter the area you want to go :")
b = raw_input("enter the your Name: ")

if a == b:
    print( ' you are good ')
elif a != b:
    print(' you are bad ')


'''
"""
for i in range(11,18):
    if i != 6:
        
        print i"""
"""        
while True:
    s = raw_input('enter the string:')
    if s == 'quit':
        break
    print 'length of the string is :', len(s)
print ('Done')"""

'''
for i in range(1,40):
    if i <=20:
        print " hello "
    elif i >= 21:
        print " chalo"
    else:
        print " over"
        
        
       '''
       
'''       
a = [121, 132,145, 1334, 1453,12225,12,13,14,15,16,17,21,31]
b = [ 21,22,32,43,23,45,36,37,38,39,40]

for i in a:
    if i == 17:
        print i
        for i in b:
            if i <=40:
                print i 


'''
'''
a = [ "hello", "chalo","come","go"]

b = ["hello", "chalo","come","go", "good","bad","fine"]
for i in a:
    for i in b:
        if a==b:
            print "nice"
        elif a!=b:
            print "worst"
        else:
            print " bad" 
            '''
"""
while True:
    s = raw_input('enter something: ')
    if s == 'quit':
        break
    if len(s)<=3:
        print "too small"
        continue
        print('input is sufficent length' ) """
        
"""
a = [ "hello", "chalo","come","go"]

b = ["hello", "chalo","come","go", "good","bad","fine"] 

for i in a:
    for i in b:
        if a == b:
    
            a + b """

            
"""         
a = raw_input("enter the message:")
b = range(1,100)


for i in b:
    if i<=b:
        print  a 
        
        i+=1
"""
"""
#Mean
a = [21,22,32,43,23,45,36,37,38,39,40]

b = int(input(" enter the average of the number need to be find :"))
c = []
for i in range(b):
    c.append(a[i])
print c
Mean = sum(c)/b 

print Mean 
"""
#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)

a =[]
#b =[]

for i in range(1500,2700):
    if (i%7==0)& (i/5==0):
        a.append(i)
    
    
print a






