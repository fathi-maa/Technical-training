n=int(input("enter the number of elemnets : "))
arr=[]
for _ in range(n):
    num=int(input("enter the elements of an array : "))
    arr.append(num)
print(arr)
largest=arr[0]
smallest=arr[0]
secondl=-1
seconds=-1
for i in range(1,n):
    if arr[i] > largest:
        secondl=largest
        largest=arr[i]
    elif arr[i] > secondl and5 arr[i]!= largest:
        secondl=arr[i]
print("second largest in the array is :", secondl)

for i in range(1,n):
    if arr[i] < smallest:
        seconds=smallest
        smallest=arr[i]
    elif arr[i] < seconds and arr[i] != smallest:
        seconds=arr[i]
print("second smallest in the array is :", seconds)

