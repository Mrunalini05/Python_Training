#ip: [4,8,14,22,36,68]
#largest nonprime b/w two numbers
#7 13 19 31 67
#sum: 137

#ip: [14,16,20,22]
# 0 19 0
#sum: 19

def isprime(n):
    if n==1 or n==2:
        return 1
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 0
    return 1
            
def largest_prime(n,m):
    for i in range(m-1,n,-1):
        if(isprime(i)):
            return i
    return 0
    
l=[4,8,14,22,36,68]
s=0
for i in range(len(l)-1):
    s+=largest_prime(l[i],l[i+1])
print(s)
