def linear(arrr,n,target):
    for i in range(n):
        if arrr[i]==target:
            return i
    return -1
num=int(input("enter the number of elements in the array : "))
arrr=[]
for _ in range(num):
    ele=int(input("enter the elements to the array:"))
    arrr.append(ele)
print(arrr)


target=20
n=0
for _ in arrr:
    n+=1
print(n)
res=linear(arrr,n,target)
if res !=-1:
    print("the target element found")
else:
    print ("the tagget elemnet not found")