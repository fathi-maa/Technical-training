def vehicle(n,w):
    for x in range(n+1):
        y=n-x
        if 4*x + 2*y == w:
            return x,y
    return None

n=10
w=28
res=vehicle(n,w)
print(res)
if res:
    print("four wheeler : " ,res[0] ,"and two wheeler :",res[1])