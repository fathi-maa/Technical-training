#occurence of letter in word
s="Baffooon"
letter={}
for l in s:
    letter[l]=letter.get(l,0)+1
print(letter)
print(letter.values())
print(letter.keys())