import math
def distance(x1, x2,y1, y2):
    return 0.0
   
def distance(x1,x2,y1,y2):
    
    dx = x2 - x1
    dy = y2- y1
    print " dx is", dx
    print " dy is ", dy
    return 0.0

def distance( x1,x2,y1,y2 ):
    dx = x2 - x1
    dy = y2- y1
    dsquared = dx**2 + dy**2
    print 'dsquared is: ', dsquared
    result = math.sqrt(dsquared)
    return result
print distance( 21,30,40,50)
#def distance( x1,x2,y1,y2 ):
    #dx = x2 - x1
    #dy = y2- y1
    #dsquared = dx**2 + dy**2
    #result = math.sqrt(dsquared)
    #print result
    #return result 
    


