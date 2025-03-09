# sum of digits of a number

n=int(input("input enter the number :"))
num=n
sum=0
while num > 0:
    rem=num%10
    sum=sum+rem
    num=num//10
print(sum)
