num=int(input("enter the number : "))
if num > 1:
    for i in range(2,num):
        if num % i ==0:
            print("the is not a prime number",num)
            break
    else:
        print("the is a prime number",num)
else:
    print("the is not an prime number",num)