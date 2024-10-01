def kangaroo(x1, v1, x2, v2):
    # If one kangaroo starts ahead and moves faster, they will never meet
    if (x1 < x2 and v1 <= v2) or (x2 < x1 and v2 <= v1):
        return "no"

    # Continue looping until they meet or pass each other
    while True:
        if x1 == x2:  # If their positions are equal, return "yes"
            return "yes"
        
        # Update positions
        x1 += v1
        x2 += v2

        # If one passes the other without meeting, return "no"
        if (x1 > x2 and v1 >= v2) or (x2 > x1 and v2 >= v1):
            return "no"

# Testing with the example:
print(kangaroo(0, 3, 4, 2))  # Expected output: "yes"
