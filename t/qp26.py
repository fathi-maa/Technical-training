#perfect number
#input = 6      factors=1,2,3,6    1+2+3=6

n=int(input())
factors=[]
for i in range(1,n):
    if n%i==0 :
        factors.append(i)
if sum(factors) == n:
    print("prefect")
else:
    print("not perfect")
