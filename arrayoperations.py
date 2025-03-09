#Array operations

'''insert at beginning
n=int(input("enter the size of array : "))
arr=[int(input("enter the elements")) for i in range(n)]
print(arr)
element=int(input("enter the element to be inserted : "))
arr.insert(0,element)
print("After inserting the array is : ")
print(arr)'''

'''insert at specific position
n=int(input("enter the number of elements:"))
arr=[int(input("enter the elements")) for i in range(n)]
print(arr)
element=int(input("enter the element to be inserted : "))
pos=int(input("enter the position to be inserted : "))
arr.insert(pos-1,element)
print("After inserting the array is : ")
print(arr)'''

'''insert at the end
n=int(input("enter the number of elements in the array : "))
arr=[int(input("enter the elements into the array : ")) for i in range(n)]
print(arr)
element=int(input("enter the element to be inserted : "))
arr.append(element)
print("After inserting the array is : ")
print(arr)'''

'''delete from beginning
n=int(input("enter the number of elements in the array : "))
arr=[int(input("enter the elements to the array : ")) for i in range(n)]
print(arr)
del arr[0]
print("After deleting the array is : ")
print(arr)'''

'''deleting element at specific position
n=int(input("enter the numbe rof elemets :"))
arr=[int(input("enter the elemts to the array:")) for i in range(n)]
print(arr)
pos=int(input("enter the position from where the element to be deleted : "))
del arr[pos-1]
print("After deleting the array is : ")
print(arr)'''

'''deleting from last
n=int(input("enter the number of elements : "))
arr=[int(input("enter the elements to the array : ")) for i in range(n)]
print(arr)
arr.pop()
print("After deleting the array is : ")
print(arr)'''

'''removing first occurence of an element
n=int(input("enter the number of elements : "))
arr=[int(input("enter the elements to the array : ")) for i in range(n)]
print(arr)
element=int(input("enter the element to be removed : "))
if element in arr:
    arr.remove(element)
print(arr)'''

n=int(input("enter the number of elements : "))
arr=[int(input("enter the elements to the array : ")) for i in range(n)]
print(arr)
element=int(input("enter the element to be removed : "))
arr1=[x for x in arr if x!=element]
print("array after removing ", element, "is : ")
print(arr1)

