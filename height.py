def visibility(heights):
    count=1
    shortest=heights[0]
    for i in range(1,len(heights)):
        if heights[i] > shortest:
            count+=1
            shortest = heights[i]
    return count

n=int(input("enter the number of students : "))
heights=[int(input("enter the heights : ")) for x in range(n)]
res=visibility(heights)
print(res)
