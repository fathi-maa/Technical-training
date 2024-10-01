num=int(input("enter the number : "))
n=int(input("enter the no of times needed to multiply : "))
sum=0
for i in str(num):
    sum+=int(i)
s=n*sum
print("the final output is : ",s)
summ=0
if len(str(s)) < 1:
    print(s)
else:
    for i in str(s):
        summ+=int(i)
    print(summ)

   
