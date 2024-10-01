def odd(balloons):
    freq={}
    for balloon in balloons:
        if balloon in freq:
            freq[balloon]+=1
        else:
            freq[balloon]=1
    for balloon in balloons:
        if freq[balloon] % 2 !=0:
            return balloon
N=7
balloons=['g','r,','b','b','r','y','r','y']
print(odd(balloons))