n=int(input("enter the no of elements : "))
arr=list(map(int,input("enter the elements : ").split()))
print(arr)
for i in range(1,n):
    val=arr[i]
    j=i-1
    while j>=0 and arr[j] > val:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=val
print(arr)