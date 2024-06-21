#find the possible paths and count no.of paths for the given graph from 5to2

'''     5---------7--------4
        |          /            |    \
        |      /                |     |-------2
        |  /                    |    /
        3-------------------8
'''

def fun(i,j,c):
    l.append(i)
    if(i==j):
        print(l)
        c=c+1
        l.pop()
        return c
        return
    for i in d[i]:
        if(i not in l):
            c=fun(i,j,c)
    l.pop()
    return c
d={5:[7,3],7:[5,4,3,],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
print(fun(5,2,0))