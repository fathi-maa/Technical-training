#Array manipulations

'''largest and smallest
n=int(input("enter the number of elements : "))
arr=[int(input("enter the elements : ")) for i in range(n)]
print(arr)
max=arr[0]
min=arr[0]
for num in arr:
    if num > max:
        max=num
for num in arr:
    if num<min:
        min=num
print("the largest element is", max)
print("the smallest element is",min)

n=int(input("enter the number of elements : "))
arr=[int(input("enter the elements : ")) for i in range(n)]
print(arr)
print(max(arr))
print(min(arr))'''
