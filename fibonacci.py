n=int(input("enter the number to which fibonacci series to be find :"))
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b