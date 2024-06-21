word="aaAbcBC"
word1="AbBCab"
a=''
c=0
c1=0
for i in word:
    if(i.islower() and i not in a and i.upper() in word):
        a=a+i
        if(word.rindex(i) < word.index(i.upper())):
            c=c+1
for i in word1:
    if(i.islower() and i not in a and i.upper() in word1):
        a=a+i
        if(word1.rindex(i) < word1.index(i.upper())):
            c=c1+1
print(c)
print(c1)