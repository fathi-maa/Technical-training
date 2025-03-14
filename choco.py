'''n=int(input("enter the no of packets : "))
choco=[int(input("enter the number of chocolates : ")) for _ in range(n)]
non_zero=[]
zero_count=0
for i in choco:
    if i!=0:
        non_zero.append(i)
    else:
        zero_count+=1
res=non_zero+[0]*zero_count
print(res)'''
        
'''n=8
arr=[4,5,0,1,9,0,5,0]
non_zero=[]
zero=0
for i in arr:
    if i!=0:
        non_zero.append(i)
    else:
        zero+=1
print(non_zero+[0]*zero)'''

n=8
arr=[4,5,0,0,9,0,5,0]
non_zero=[]
for i in arr:
    if i==0:
        arr.remove(i)
        non_zero.append(i)
print(*(arr+non_zero))