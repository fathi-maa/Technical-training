n=int(input("enter the number :"))
l=len(str(n))
if n == sum([int(i)**l for i in str(n)]):
    print("it is armstrongnumber ")
else:
    print("it is not an armstrong number")
