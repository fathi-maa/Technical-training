l=[5,90,1,7,3,45,12]
dict={i:l[i] for i in range(len(l))}
print(dict)
l3=[]
for key,value in dict.items():
    l2=[90,5,12]
    for num in l2:
        if num==value:
            l3.append(key)
    
print(l3)
if l3 == sorted(l3):
    print("the list is ther")

