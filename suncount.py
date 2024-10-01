def count_sundays(start_day, n):
    # Map days to numeric values
    days_map = {"mon": 1, "tue": 2, "wed": 3, "thu": 4, "fri": 5, "sat": 6, "sun": 7}
    
    # Get the numeric value of the starting day
    current_day = days_map[start_day.lower()]
    
    # Initialize the Sunday counter
    sunday_count = 0
    
    # Loop through each day in the range
    for i in range(n):
        if current_day == 7:  # Check if it's Sunday (day 7)
            sunday_count += 1
        current_day = (current_day % 7) + 1  # Move to the next day, wrapping to Monday after Sunday
    
    return sunday_count

# Example usage
start_day = "mon"  # Starting day of the week
n = 13             # Number of days
result = count_sundays(start_day, n)
print(result)  # Expected output: 2
