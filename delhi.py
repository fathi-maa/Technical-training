n=int(input("enter the number of vehicles : "))
a=[int(input("Enter the last digit of the number plate : ")) for i in range(n)]
print(*a)
D=int(input("enter the date : "))
x=int(input("enter the fine amount : "))
count=0
if D%2==0:
    for i in a:
        if i%2!=0:
            count+=1
    s=x*count
    print("The fine amount is : ",s)
else:
    for i in a:
        if i%2==0:
            count+=1
    s=x*count
    print("the fine amount is : ",s)


