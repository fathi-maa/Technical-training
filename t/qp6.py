#leap year
'''year=int(input("enter the year : "))
if ((year%400 == 0 ) or (year%4 ==0 and year%100 !=0)):
    print("the year" , year, " is a leap year")
else:
    print("the year", year ," is not a leap year")'''


'''def is_leap(year):
    if ((year%400 == 0 ) or (year%4 ==0 and year%100 !=0)):
        return True
    return False

year=int(input("enter the year : "))
if is_leap(year):
    print("the year" , year, " is a leap year")
else:
    print("the year", year ," is not a leap year")'''

start=int(input("enter the lower bound"))
stop=int(input("enter the upper bound"))
count=0
for year in range(start , stop+1):
    if (year%400==0 or (year%4==0 and year%100!=0)):
        count+=1
print(count)
