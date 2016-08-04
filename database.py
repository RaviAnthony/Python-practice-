import anydbm
import pickle
db = anydbm.open('helo.db', 'c')
db['hero'] = 'photo of hero'
print db['hero'] 

t= [1,2,3,4]
pickle.dumps(t)
print t

t1= [1,2,3,4,5,6]
s= pickle.dumps(t1)
t2=pickle.loads(s)
print t2 
print t1

def linecount(filename):
    count = 0
    for line in open(filename):
        count +=1
    return count
print linecount('module.py')

def wordcount(filename):
    count = str('  ')
    for word in open(filename):
        count += 1
    return count 
print wordcount('module.py')
        