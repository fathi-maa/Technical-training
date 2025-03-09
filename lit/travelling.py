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
print(*result)
