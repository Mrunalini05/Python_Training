def fun(x,s):
    if(x==len(a)):
        return s
    s=s+a[x]
    t=fun(x+1,s)
    return t
a=[6,7,2,5]
print(fun(0,0))
