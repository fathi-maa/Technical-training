#nth term of fibonacci

n=int(input("enter the number"))
a,b=0,1
fib=[a,b]
for _ in range(n-2):
    c=a+b
    fib.append(c)
    a,b =b,c

print(fib[-1])