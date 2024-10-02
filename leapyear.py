year =int(input("enter the future year : "))
leap=[]
for year in range(2023,year+1):
    if(year%4==0 and (year%100!=0 or year%400==0)):
        leap.append(year)
print(*leap)