n=int(input("Enter the number of members : "))
fact=1
for i in range(1,n):
    fact=fact*i
print(fact)
s=2*fact
print("the number of ways the membres can be arranged is :",s)
