def smallest(arr):
    min_value=arr[0]
    if len(arr) == 1:
        print("There is only one element in the array")
    if all(num == arr[0] for num in arr):
        print("all the elements are same")
    if all(num == 0 for num in arr):
        print("all the elements are zero")
    for num in arr:
        if num < min_value:
            min_value = num
    return min_value
n=int(input("enter the number of elements in array"))
arr=[int(input("enter the elements")) for i in range(n)]
res=smallest(arr)
print(res)
