N=int(input("enter the number of vehicles :"))
a=[int(input("enter the reg number : ").strip()) for i in range(N)]
date=int(input("enter the date : "))
X=int(input("enter the fine : "))
count=0
for reg in a:
    if (date%2==0 and reg %2 !=0) or (date%2!=0 and reg%2==0):
        count+=1
fine=X*count
print(fine)
