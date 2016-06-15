def add(a,b):
    print"add %d+%d"%(a,b)
    return a+b
def sub(a,b):
    print"sub %d - %d" %(a,b)
    return a-b
def mul(a,b):
    print"mul %d * %d" %(a,b)
    return a*b
def div(a,b):
    print("div %d / %d")
    return a/b


print" let do some mathematical functions"

age=add(35,12)
height=sub(75,52)
weight=mul(25,4)
iq=div(48,3)

print"age %d, height %d,weight %d,iq %d."%(age,height,weight,iq)

print" puzzle begins"

What= add(age,sub(height,mul(weight,div(iq,5))))

print" that becomes what can you do it by your hands"