curtains=input("enter the curtain string : ")
s=len(curtains)
L=int(input("enter the value for L : "))
cur_groups=[curtains[i:i+L] for i in range(0,s,L)]
for i in cur_groups:
    a_count=i.count('a')
max_a=max(a_count)
print(max)
