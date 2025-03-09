l1=[1,2,3]
l2=[]
fact=1
for num in l1:
    fact=1
    for j in range(1,num+1):
        fact=fact*j
    l2.append(fact)
print(l2)
