a = 1
b = 2
c = a + b
s = b

while c < 4000000 :
    if (c % 2 == 0) :
        s = s + c
    a = b
    b = c
    c = a + b
print s