states = {'Telangana':'TS','Andhra':'A','Tamilnadu':'TN','Delhi':'D'}

cities ={ 'hyderabad':'hyd','vijayawada':'vz', 'Madras':'M', 'Nizam':'NZ'}
cities['TS'] = 'Secundrabad'
cities['A'] = ' warangal'

print '-' *10
print "TS State has:", cities['TS']
print " A State has :", cities['A']


print '-'*10

print " Telangana's abbrev is : ", states['Telangana']
print "Tamilnadu's abbrev is : ", states['Tamilnadu']

print '-'*10

print " Telangana's abbrev is : ", cities[states['Telangana']]
print "'Andhra' abbrev is : ", cities[states['Andhra']]

print '-'*10

for state, abbrev in states.items():
    print"%s is abbrev %s" %(state,abbrev)
    
print '-'*10

for cities, abbrev in cities.items():
    print"%s is abbrev %s" %(cities,abbrev)

print '-'*10

#for state, abbrev in states.items():
   # print "%r state is abbrev %r and has city %r" % (state, abbrev, cities[abbrev])

print '-'*10

State = State.get('Telangana', None)


if not State:
    print"sorry, no Telangana"
    
city= cities.get('TS','Does  not exit')
print "The city for the state 'TS'is: %s" %city

    
    


    
