n=int(input("enter the range of numbers :"))
sums=[]
for i in range(n):
    if i > 1:
        for x in range(2,i):
            if i%x==0:
                break
        else:
            sums.append(i)
total=sum(sums)
print("sum is ",total)