num=int(input())
if num<2:
    print("not an prime")
else:
    for i in range (2, int(num**0.5)+1):
        if num%i==0:
            print("not a prime")
            break
        
    else:
        print(num ,"is a prime")
    