#a^b=c
#if b=?then, a^c=b
encoded=[1,2,3]
first=1
r=[first]
for i in range(len(encoded)):
    r.append(encoded[i]^r[i])
print(r)