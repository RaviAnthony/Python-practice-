def fabc (n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        n = (n-1)+(n-2)
        return n
       
       
print fabc(20)
