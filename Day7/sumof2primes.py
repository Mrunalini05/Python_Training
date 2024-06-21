# sum of both prime numbers to get the given number

def isprime(x):
    if(x==1):
        return 1
    if(x==2):
        return 1
    for i in range(2,(x//2)+1):
        if(x%i==0):
            return 0
    return 1

n=int(input())
for i in range(1,(n//2)+1):
    if(isprime(i) and isprime(n-i)):
        print("yes")
        print(i,n-i)
        break
else:
    print("no")