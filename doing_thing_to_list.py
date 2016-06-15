ten_things= "Apple orange mango crows telephone light sugar"

print "wait  there are not 10 things in the list, let fix that."

stuff = ten_things.split(' ')
more_stuff = [ " hi", "helo", "hey","join", " rey", "list", "banana", "chalo"]

while len(stuff) != 10:
    next_one=more_stuff.pop()
    print"Adding:",next_one
    stuff.append(next_one)
    print " number of items %d" %len(stuff)

print "there we go: ", stuff
print "let's do some things with stuff"


print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print'#'.join(stuff[3:5])