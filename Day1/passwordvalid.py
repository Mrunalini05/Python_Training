'''ip: asd123!@#
op: 1 (upcase)
ip: 123456789
op: 3
ip:ab
op: 6
ip:A1234B
op:2
ip: A123a@4
op:-1
ip: a123456
op: 2'''


n=input()
up,lw,d,s=1,1,1,1
if(8-len(n)>4):
        print(8-len(n))
else:
    for i in n:
        if i.isalpha() and i.isupper():
            up=0
        elif i.isalpha() and i.islower():
            lw=0
        elif not i.isalnum():
            s=0
        elif i.isdigit():
            d=0
    sum=up+lw+s+d
    if sum>0:
        print(sum)
    else:
        print(-1)