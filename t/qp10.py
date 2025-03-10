# vending machine assigns unique code to its snacks. each code is a number. when a customer select a snack, 
# vending machine scans the code and calculate price by multiplying all digits in the N
#  if input is 1223 then output is 12

N=int(input("enter the code : "))
mul=1
num=N
while num>0:
    rem=num%10
    mul=mul*rem
    num=num//10
print(mul)