def Sunday(day, n):
    map = {
        "monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4,
        "friday": 5, "saturday": 6, "sunday": 7
    }
    
    start = map[day.lower()]
    sunday_count = 0
    
    for i in range(n):
        current_day = (start + i - 1) % 7
        if current_day == 0:  # Since current_day == 0 corresponds to Sunday
            sunday_count += 1
    
    return sunday_count

day = input("Enter the day to start: ")
n = int(input("Enter the number of days: "))
res = Sunday(day, n)
print(res)
