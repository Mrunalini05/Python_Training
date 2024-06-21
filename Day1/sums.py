'''ip: 5 3.8 7 5.6 4 2 3
op: evensum:6
      oddsum:15
      decimal:9.4'''

l=input().split()
es,os,ds=0,0,0
for i in l:
    if i.isdigit():
        n=int(i)
        if n%2==0:
            es=es+n
            n=n+1
        elif not n%2==0:
            os=os+n
            n=n+1
    else:
        a=float(n)
        ds=ds+a
        a=a+1
print(es)
print(os)
print(ds)