#ip: MMFFMFFMFMFMFFMMFFMMF"
#op: M> print-M
#      F> print-F
#      bothequal= print-0
str=input()
c=0
for i in str:
    if i=='M':
        c=c+1
    else:
        c=c-1
print(c)
if c==0:
    print('0')
elif c>0:
    print('M')
else:
    print('F')