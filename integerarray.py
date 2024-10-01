def integerarray(num):
    count=1
    greater=num[0]
    for i in range(1,len(num)):
        if num[i] > greater:
            count+=1
            greater = num[i]
    return count


n=int(input("enter the no of integers : "))
num=[int(input("enter the values : ")) for x in range(n)]
res=integerarray(num)
print(res)