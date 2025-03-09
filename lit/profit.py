stock=list(map(int , input("enter").strip().split()))
profit=0
for i in range(1,len(stock)):
    if stock[i] > stock[i-1]:
        deff = stock[i] - stock[i-1]
        profit+=deff

print(profit)