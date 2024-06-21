'''def fac(x):
    if(x==1):
        return 1
    return x*fac(x-1)
print(fac(5))
'''


'''#sum of evennumbers in 1to10
def fun(x):
    if(x==0):
        return 0
    return x+fun(x-2)
print(fun(10))
'''

#sum of even nd odd numbers in 1to13
def fun(x):
    if(x==0):
        return 0
    return x+fun(x-2)
#print(fun(13))
n=13
if(n%2==0):
    print(fun(n))
else:
    print(fun(n-1))