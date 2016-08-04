
a = raw_input("enter the string:")

def strcon(a):
    
    b = a.replace(" ", "")
    c = a.upper()
    d = a.lower()
    for i in a:
        e= a.count(i)
        print e 
    print b
    print c
    print d 
strcon(a)
    
