# check whether armstrong number
num=int(input())
l=len(str(num))
N=num
arm=0
while N>0:
    rem=N%10
    arm=arm+rem**l
    N=N//10
if num == arm:
    print("armstrong")
else:
    print("not an armstrong")