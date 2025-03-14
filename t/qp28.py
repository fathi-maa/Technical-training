#A chocolate factory is packing chocolates into the packets. The chocolate packets here represent an array  of N number of integer values. 
# The task is to find the empty packets(0) of chocolate and push it to the end of the conveyor belt(array).8  – Value of N
 #      input N-8 arr=[4,5,0,1,9,0,5,0]   Output:4 5 1 9 5 0 0 0

'''try:
    n=int(input())
    zero=[]
    non_zero=[]
    arr=list(map(int , input().split(",")))
    for i in arr:
        if i==0:
            zero.append(i)
        else:
            non_zero.append(i)
    output=non_zero+zero
    print(*output)
except EOFError:
    print(0)
 '''

try: 
    n=int(input())
    zero=[]
    arr=list(map(int , input().split(",")))
    for i in arr:
        if i == 0:
            arr.remove(i)
            zero.append(i)
    print(*(arr+zero))
except EOFError:
    print(0)
