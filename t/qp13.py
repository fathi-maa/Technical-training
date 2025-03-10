# a gift shop asiigns unique code for each of the gift,represented as string.some characters in the tag may be repeated 
# while others apperas only once.task is to determine number of non repeating characters in a given gift tag 
# the input is like google then output 2

code=input("enter the code :")
number={}
for l in code:
    number[l]=number.get(l,0)+1
print(number)
count=0
for value in number.values():
    if value==1:
        count+=1
print(count)