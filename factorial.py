n=int(input("enter the number to find factorial : "))
fact=1
if n<0:
    print("fcatorial doesn't exist for negetive numbers")
elif n==0:
    print("factorial of zero is 0")
else:
    for i in range(1,n+1):
        fact*=int(i)
    print(fact)