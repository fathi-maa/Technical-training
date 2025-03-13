# armstrong number in a range

u=int(input())
l=int(input())
count=0
for num in range(u,l+1):
    num1=num
    le=len(str(num))
    arm=0
    while num>0:
        rem=num%10
        arm=arm+rem**le
        num=num//10
    if num1 == arm:
        count+=1
print(count)



