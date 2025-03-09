def isvalid_paranthesis(s):
    stack=[]
    map={')':'(' , ']':'[' , '}':'{'}
    for char in s:
        if char in map:
            top=stack.pop()
            if map[char] != top:
                return False
        else:
            stack.append(char)
    return not stack
s="(){}[]"
print(isvalid_paranthesis(s))

n=int(input("enter the number of cities : "))
visit =list(map(int , input("enter the number of times : ").strip().split()))
cities = []
for i in range(n):
    if visit[i] > 0 :
        cities.append(visit[i])
print(cities)
result=[]
prev=None
while sum(visit) > 0:
    best = -1
    max = -1
    for i in range(n):
        if visit[i] > max and i+1 != prev:
            best = i+1
            max = visit[i]
    result.append(best)
    visit[best-1]-=1
    prev = best
print(len(result))

stock=list(map(int,input("enter stock prices : ").strip().split( ",")))
buying_price=stock[0]
profit = 0
for price in stock[1:]:
    if price < buying_price:
        buying_price=price
    elif (price-buying_price) > profit:
        profit = price-buying_price
print(profit)

prices=list(map(int,input("enter the prices : ").split()))
long=[]
curr=[prices[0]]
for i in range(1,len(prices)):
    if prices[i] > prices[i-1]:
        curr.append(prices[i])
    else:
        if len(curr )> len(long):
            long = curr
        curr=[prices[i]]
if len(curr )> len(long):
    long = curr
print(*long)

