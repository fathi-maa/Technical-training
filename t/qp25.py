# strong number = sum of factorial of the digits is the original number
# input =145 1!=1  4!=24   5!=120

n=int(input())

output=[]
while n>0:
    rem=n%10
    fact=1
    for i in range(1,rem+1):
        fact*=i
    output.append(fact)
    n//=10
print(sum(output))

