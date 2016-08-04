fopen = open("abc.txt")
s = fopen.read()
s1=str(s)
s2=s1.split(" ")
d={}
for i in s2:
    d[i] = d.get(i,0)+1
 
for i in d:
    
    print d[i], i
    s3=str(d[i])
    s4= s3.sort()
    
print s4 