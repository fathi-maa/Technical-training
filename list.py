l=[2,5,6,3,9,4]
target=9
pair=[]
seen=set()
for num in l:
    diff = target-num
    if diff in seen:
        pair.append((diff,num))
    else:
        seen.add(num)
print(pair)
