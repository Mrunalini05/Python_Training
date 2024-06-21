#ip: xyzabcdefklmnopqefgh
#op: print the longest length of subsequence- 7: klmnopq


str=input()
c=1
max=0
for i in range(len(str)-1):
    if(ord(str[i])==ord(str[i+1])-1):
        c=c+1
    else:
        if(c>max):
            max=c
        c=1
if(c>max):
    max=c
print(max)