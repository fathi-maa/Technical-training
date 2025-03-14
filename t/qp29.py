#A positive integer has been given as an input. Convert decimal value to binary representation. Toggle
# all bits of it after the most significant bit including the most significant bit. Print the positive integer value after toggling all bits
try:
    n=int(input())
    leng=n.bit_length()
    mask=(1<<leng)-1
    toggle=n^mask
    print(toggle)
    print(bin(n)[2:].zfill(leng))
    print(bin(toggle)[2:].zfill(leng))
except EOFError:
    print(0)
    