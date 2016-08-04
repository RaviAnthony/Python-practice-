""" import tuple.py

def linecount(filename):
    count = 0 
    for line in open(filename):
        count += 1
        return count
print linecount('tuple.py')"""



hello = [5,6,9,10]
challo = [5,6,9,10]

print hello

print challo

def compare(x,y):
    if set(hello) & set(challo):
        print " number are found"
    else:
        print " not found"
        
print compare(hello,challo)