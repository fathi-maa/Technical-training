#fibonacci series

n=int(input("enter the numbe rof terms : "))
a,b = 0,1
fib=[a,b]
for _ in range(n-2):
    c=a+b
    fib.append(c)
    a,b=b,c
print(*fib)
