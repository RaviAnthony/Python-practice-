a=[1,1,1,1,1,1,1,1,2,3,4,5,4,4,4,4,3,4,5]


for idx,i in enumerate(a):
    if i not in a[:idx]:
        c = a.count(i)
        print i , c