#fibanocci series in recursion
'''def fun(x):
    if(x==0):
        return 0
    if(x==1):
        return 1
    if(x==2):
        return 1
    return fun(x-1)+fun(x-2)
print(fun(4))'''



def fun(x):
    if(x==0):
        return 0
    if(x==1):
        return 1
    if(x==2):
        return 1
    return fun(x-1)+fun(x-2)

for i in range(10):
    print(fun(i),end=' ')