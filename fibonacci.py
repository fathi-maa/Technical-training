'''n=int(input("enter the number to which fibonacci series to be find :"))
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b'''

''' fibonacci series upto which the sum should be less than or equal to 30'''
a, b = 0, 1
sum_fib = 0

print("Fibonacci series where the sum is less than or equal to 30:")

while sum_fib + a <= 55:
    print(a, end=" ")
    sum_fib += a
    a, b = b, a + b