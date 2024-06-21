#ip: a=[3,8,5,4,3]
#b= [5,0,9,3,2]
#op: (12,17)

'''def even(x,s):
    if(x==len(a)):
        return s
    if(a[x]%2==0):
        s=s+a[x]
    t=even(x+1,s)
    return t
def odd(x,s):
    if(x==len(b)):
        return s
    if(b[x]%2!=0):
        s=s+b[x]
    t=odd(x+1,s)
    return t
a=[3,8,5,4,3]
b=[5,0,9,3,2]
print(even(0,0),odd(0,0))
'''

'''def fun(x,s1,s2):
    if(x==len(a)):
        return s1,s2
    if(a[x]%2==0):
        s1=s1+a[x]
    if(b[x]%2!=0):
        s2=s2+b[x]
    return fun(x+1,s1,s2)
a=[3,8,5,4,3]
b=[5,0,9,3,2]
#print(fun(0,0,0))
x,y=fun(0,0,0)
print(x,y)
'''


#sum of even numbers in 1to10
def even(x,s):
    if(x==10):
        return s
    if(x%2==0):
        s=s+x
    t=even(x+1,s)
    return t
print(even(0,0))