from sys import argv
script,filename = argv

print"we are going to earse %r" %filename
print"helo what are you doing"
print" doing nothing"

raw_input("?")

print"opening the file"
target=open(filename,'w')
print"truncating the file. goodbye!"
target.truncate()
print"now I am going to ask you three lines."
line1=raw_input("line 1:")
line2=raw_input("line 2:")
line3=raw_input("line 3:")

print" i am going to write this line to file."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print"And finally,we close it."
target.close()