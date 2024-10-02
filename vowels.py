s=input("enter the string")
arr1=[]
arr2=[]
for x in s:
    if x in 'aeiou':
        arr1.append(x)
    else:
        arr2.append(x)
print("vowels" , arr1)
print("consonents :",arr2)