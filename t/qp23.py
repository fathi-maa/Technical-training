# prime factor 
n=int(input())
factor=[]
for i in range(1,n+1):
    if n%i==0:
        factor.append(i)
prime=[]
for num in factor:
    if num<1:
        continue
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            break
    else:
            prime.append(i)
print(prime)