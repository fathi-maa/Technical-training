
    
n=int(input("enter the number of elemts in the array: "))
arr=[]
for _ in range(n):
    num=int(input("enter the elements to the array : "))
    arr.append(num)
print(arr)
largest=arr[0]
smallest=arr[0]
for i in range(1,n):
    if arr[i]>largest:
        largest=arr[i]
print("the largest element is",largest)
for i in range(1,n):
    if arr[i]<smallest:
        smallest=arr[i]
print("the smallest element is",smallest)
        
