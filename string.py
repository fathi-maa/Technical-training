# Input string
S = input("Enter the string consisting of '*' and '#': ")

# Count occurrences of '#' and '*'
count_hash = S.count('#')
count_star = S.count('*')

# Compare counts and determine the result
if count_hash == count_star:
    print("0 -> number of '*' and '#' are equal")
elif count_star > count_hash:
    print(f"{count_star - count_hash} -> positive integer (more '*')")
else:
    print(f"{count_hash - count_star} -> negative integer (more '#')")
