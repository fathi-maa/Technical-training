'''n=int(input("enter the number"))
rev=0
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n//=10
print (rev)'''

n=input("enter the number :123")
print(n[::-1])

