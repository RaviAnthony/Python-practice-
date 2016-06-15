"""known = {0:0, 1:1}
fibonacci = n
def fibonacci(n):
    if n in known:
        return known[n]
    else:    
        res = fibonnaci(n-1)+fibonacci(n-2)
        known[n] = res
        return res
print fibonacci(10)   """ 





u=raw_input()
n=int(u)
a=[0 for x in range(n)]
a[0]= 0
a[1]= 1

print a[0]
print a[1]
for i in range(2,n):
    a[i] = a[i-1] + a[i-2]
    print a[i]