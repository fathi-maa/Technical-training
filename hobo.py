'''n=50
p=48
c=n-p
if p < c:
    print(p)
else:
    print(c)'''

'''n = 50  # Total number of pages
p = 48  # Target page
num=n//2
if num <=p:
    ans=n-p
else:
    ans=p
print(ans)'''

n=50
p=48
print(min(p//2,n//2-p//2))