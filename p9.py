n=int(input("enter the number : "))
is_prime=True
for i in range(2,int (n**0.5)+1):
    if n%i==0:
       is_prime=False
       break
if is_prime and n>1:
    print("prime")
else:
    print("not")