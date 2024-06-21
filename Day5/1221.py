s="RLRRLLRLRL"
s1=0
c=0
for i in s:
    if i=='R':
         c=c+1
    else:
         c=c-1
    if c==0:
         s1=s1+1
print(s1)