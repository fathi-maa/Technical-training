# Given an integer array Arr of size N the task is to find the count of elements whose value is greater than all of its prior elements.
# input  n= 5 Arr[]={7,4,8,2,9} output =3
'''try:
    n=int(input())
    arr=[int(input()) for i in range(n)]
    count=1
    short=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>short:
            count+=1
            short=arr[i]
    print(count)
except EOFError:
    print(0)
'''

try:
    n=int(input())
    if not (1<=n<=20):
        print("invalid")
        exit()
    arr=[]
    num=int(input())
    if not (1 <= num <= 10000):
        print("invalid")
        exit()
        arr.append(num)
    count=1
    short=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>short:
            count+=1
            short=arr[i]
    print(count)
except EOFError:
    print(0)