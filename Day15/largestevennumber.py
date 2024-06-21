#find the largest possible even number
#ip: tu5g2k1h8
#     g5g8gd6h3
# without duplicates the number is 521863
#op: 865312

s1="tu5g2k1h8"
s2="g5g8gd6h3"
n=0
l=[]
s=list(s1+s2)
#print(s)
for i in s:
    if i not in l and i.isdigit():
        l.append(i)
a=sorted(l,reverse=True)
#print(''.join(a))
print(a)
if(int(a[-1])%2==0):
    print(''.join(a))
else:
    for i in range(len(a)-2,-1,-1):
        if(int(a[i])%2==0):
            a.append(a.pop(i))
            print(''.join(a))
            break
    else:
        print(-1)