n=int(input("enter the positive integer : "))
bits=n.bit_length()
print(bits)
a=(1 << n.bit_length()) - 1
res = n ^ a
print(res)
print(bin(res)[2:])
