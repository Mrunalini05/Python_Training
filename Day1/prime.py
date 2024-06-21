'''ip: 13
op: prime
      13

ip: 14
op: notprime
      17'''

'''n=13
c=0
for i in range(2,(n//2)+1):
    if(n%i==0):
        c=c+1
        break
if(c==0):
    print("prime")
else:
    print("np")'''


n=int(input())
while(1):
    c=0
    for i in range(2,(n//2)+1):
        if(n%i==0):
            c=c+1
            break
    if(c==0):
        print(n)
        break
    else:
        n=n+1
    

'''n=int(input())
f=0
for i in range(2,n//2+1):
    if n%i == 0:
        f=1
        break
if(f==1):
    while(True):
        n=n+1
        f=0
        for i in range(2,n//2):
            if n%i == 0:
                f=1
                break
        if(f==0):
            print(n)
            break
else:
    print(n)'''