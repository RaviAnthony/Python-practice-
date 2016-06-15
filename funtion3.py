"""def do_twice(f):
    f()
    f()
    
def print_spam():
    print 'spam'
    print " i don't know"
    add = 10 + 12
    print " add = %d " %add
    helo = " plz don't irritate me "
    print " %s " % helo
    print " get up don't get low"
    
do_twice(print_spam)"""

def print_number(n):
    if n  <= 10:
        print n
        print_number(n+1)

        
print_number(1)