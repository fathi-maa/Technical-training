#palindrome
a=121
num=a
rev=0
while num>0:
    r=num%10
    rev=rev*10 + r
    num=num//10
if rev== a:
    print("palindrome")
else:
    print("not palindrome")
