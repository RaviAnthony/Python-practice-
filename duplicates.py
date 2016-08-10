
a = [1,1,1,1,2,3,4,5,4,4,4,4,3,4,5]
def remove_duplicates(x):
    b = []
    for i in x:
        if i not in b:
            b.append(i)
            b.sort()
        return b
    
print remove_duplicates(a)




"""a=[1,1,1,1,1,2,3,4,5,4,4,4,4,3,4,5]
b =int(input("Enter a number: "))
print "Count for b : ", a.count(b)

"""

"""a=[1,1,1,1,1,2,3,4,5,4,4,4,4,3,4,5]
b= set(a)
for i in b:
    c = a.count(i)
    print i , c"""

    

