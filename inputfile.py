fabc= open("vijay.txt", 'w')
print fabc

line1 = " This is a cat. This is a dog. This was on the table. The table is very long. Cat is a nice pet. Dot is a nice pet"
fabc.write(line1)
fabc.close()

a=open("vijay.txt", 'r')
b={}
#print dir(a)
for i in a:
    if i not in b:
        b.append(i)
        print b
        