# input  5,2,3,4,7,8,6   output  2,3,4,7,8
prices=list(map(int,input("enter the prices : ").split()))
long=[]
curr=[prices[0]]
for i in range(1,len(prices)):
    if prices[i] > prices[i-1]:
        curr.append(prices[i])
    else:
        if len(curr )> len(long):
            long = curr
        curr=[prices[i]]
if len(curr )> len(long):
    long = curr
print(*long)
        