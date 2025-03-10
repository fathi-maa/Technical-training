#numberof words in the sentence

sentence="my name is fathima and my fathima is good"
word={}
for w in sentence.split():
    word[w]=word.get(w,0)+1
print(word)