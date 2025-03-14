# square root
try:
    n=int(input())
    if int(n**0.5)**2 == n:
        print (n , "is the perfect number")
    else:
        print(n,"is not a perfect numebr")
except EOFError:
    print(0)