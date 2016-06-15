bye=dict()
print bye

cera={'helo':'chalo', 'bye': 'cye', 'jack':'jack'}
pera = {'celo':'halo', 'rye': 'gye', 'mack':'lack'}
print cera

print cera['bye']

print cera['jack']

print cera['helo']
    
c=len(cera)
print c

b = 'full' in cera
print b

vals = cera.values()
'helo' in vals
print vals 

def club(cera, pera):
    club = cera.update(pera)
    print cera


print club(cera, pera) 


print cera    

cera.pop('helo')
print cera
    
cera.pop('celo', 'mack')
print cera
