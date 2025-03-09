'''sum of natural
n=int(input("enter the number of natural numbers to add"))
sum=0
arr=[]
for i in range(1,n+1):
    sum+=i
    arr.append(i)
print(arr)
print(sum)'''

'''factorial
n=int(input("enter the number : "))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)'''

''''palindrome number
n=int(input ("enter the number : "))
num=n
rev=0
while n != 0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)'''

'''reversing strinh
word = input("enter the word to swap : ")
n=0
for letter in word:
    n+=1
print(n)
w=list(word)
start=0
end=n-1
while(start < end):
    temp=w[start]
    w[start]=w[end]
    w[end]=temp

    start+=1
    end-=1
print(*w)'''

''''prime munber
n=int(input("enter the input :"))
if n > 1:
    for i in range(2,n):
        if n % i == 0 :
            print("not a prime number ")
            break
    else:
        print ("prime number ",n )
else:
    print("not a prime")'''

'''#count the letters in word
num = int(input("Enter a number: "))
count = 0
while num !=0:
    count+=1
    num=num//10

print(count)'''

