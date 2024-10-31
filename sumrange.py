#Sum of numbers in a given range
l=int(input("enter the lower bound :"))
u=int(input("enter the upper bound:"))
sum=0
for i in range(l,u+1):
    sum=sum+i
print(sum)