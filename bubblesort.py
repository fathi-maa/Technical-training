n=int(input("enter the number of elemnts in the array : "))
arr=[]
for _ in range(n):
    num=int(input("enter the elemts to the array : "))
    arr.append(num)
print(arr)

for i in range(1,n):
    for j in range(0,n-i):
        if arr[j]> arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print (arr)