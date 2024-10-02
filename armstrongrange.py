n = int(input("Enter the upper range: "))

# Loop through the range and check for Armstrong numbers
for num in range(10, n + 1):  # Starting from 10, as single-digit numbers are trivial
    l = len(str(num))  # Find the number of digits in num
    if num == sum([int(i)**l for i in str(num)]):  # Check if it's an Armstrong number
        print(f"{num} is an Armstrong number")
