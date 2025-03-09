stock=list(map(int,input("enter stock prices : ").strip().split( ",")))
buying_price=stock[0]
profit = 0
for price in stock[1:]:
    if price < buying_price:
        buying_price=price
    elif (price-buying_price) > profit:
        profit = price-buying_price
print(profit)
'''stock = list(map(int, input().split(",")))

buying_price = stock[0]
profit = 0

for price in stock[1:]:  # Start from the second element
    buying_price = min(buying_price, price)  # Update buying price if a lower value is found
    profit = max(profit, price - buying_price)  # Update profit if a higher difference is found

print(profit)
'''