from sys import argv
from os.path import exists

scripts, from_file, to_file = argv

print " copying from %s to %s" %(from_file, to_file)

in_file=open(from_file)
indata=in_file.read()

print" the input file is %d byte long" % len(indata)
print"does the file out exist %r" %exists(to_file)

print"ready, hit return to continue, ctrl-c to abort."
raw_input()

out_file=open(to_file,'w')
out_file.write(indata)

print"alright all done"
out_file.close()
in_file.close()
