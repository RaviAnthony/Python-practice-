print"let's practice everything."
print 'you \'d need to know \'bout the escapes with\\ that do\n newlines and \t tabs.'
poem="""

\t the worldfaghdvhbdj \n jkdgbksbg \dugksangngna \n\t there is nothing """

print"-----------------"
print poem
print"----------------"

five=10+2+3-5
print" this should be five:%s" %five

def secret_formula(started):
    jelly_beans = started*500
    jars = jelly_beans/1000
    crates = jars/100
    return jelly_beans,jars,crates

start_point = 1000
beans, jars,crates = secret_formula(start_point)

print" with a starting point of :%d." % start_point
print"we would have %d beans,%d jars and %d crates." %(beans,jars,crates) 

start_point = start_point/10

print"we can also do that this way:"
print"we would have %d beans,%d jars and %crates."%secret_formula(start_point)

