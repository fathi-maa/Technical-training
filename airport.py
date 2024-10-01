n=int(input("enter the number of bags dumped : "))
risk=[int(input("enter the risk factor associated with each bag : ")) 
      for x in range(n)]
res=sorted(risk)
print(*res)
