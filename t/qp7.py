#prime number within a range
a=int(input("enter the lower bound : "))
b=int(input("input the upper bound : "))
count=0
for num in range(a,b+1):
    if num<2:
        continue
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                break
        else:
            count+=1
print(count)