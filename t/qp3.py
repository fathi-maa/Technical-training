
#sum of n natural numbers

# n=int(input("enter the numbe rof elements : "))
# ele = [int(input("enter the numbers : ")) for i in range(n)]
ele =list(map(int, input("enter the numbers : ").split()))
summ=0
for i in ele:
    summ=summ+i

#summ=sum(ele)
print(summ)
