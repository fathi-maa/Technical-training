#Airport security officials have confiscated several item of the passengers at the security check point. All the items have been dumped 
# into a huge box (array). Each item possesses a certain amount of risk[0,1,2]. Here, the risk severity of the items represent an array[] of
# N number of integer values. The task here is to sort the items based on their levels of risk in the array. The risk values range from 0 to 2.
# input n= 10 arr=[1,0,2,0,1,0,2] output = 0 0 0 1 1 2 2  
try:
    n=int(input())
    arr = [int(input()) for i in range(n)]
    arr.sort()
    print(arr)
except EOFError:
    print(0)
