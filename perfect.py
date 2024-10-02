n=int(input("enter the number : "))
sum=0
if n <=0:
    print("the perfect numbers are positive integers")
else:
    for i in range(1,n):
        if n % i ==0:
            sum+=i
if n==sum :
    print ("it is perfect number" )
