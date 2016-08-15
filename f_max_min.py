
"""
def max_min(a,b):
    if a > b:
        return a, " max number" 
    elif a < b:
        print b,"max number"
    elif a == b:
        print"both are  equal"
    else:
        print"try again"
        
max_min(19,21)


"""
"""


def max_min(a,b):
    if a > b:
        return '{ravi} is greater than {helo}'.format(ravi=a,helo=b) 
    elif a < b:
        print(b,"max number")
    elif a == b:
        print("both are  equal")
    
    else:
        print("try again")
        
print max_min(19,10)

"""
"""
#Local variable


x = 50 

def func(x):
    print x
    x = 2 
    print 'Changed local x to',x
    
func(x)   
print 'x is still', x
"""
"""
#global variable

x = 50 

def func():
    global x
    print x , "x is"
    x = 2 
    print 'Changed global x to',x
    
func()   
print 'x is still', x


"""
"""
#default argument values 

def say(message,times=1):
    print message*times
say('love u ')    
say('hate u ', 5)

"""
"""
#return

def maximum(x,y):
    if x > y :
        return x
    if x < y:
        return y
print maximum(20,35)


"""





    















