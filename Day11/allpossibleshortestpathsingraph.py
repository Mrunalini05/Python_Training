#find all the possible paths for the given graph from 5to7, 5to3, 5to4, 5to8, 5to2

'''     5---------7--------4
        |          /            |    \
        |      /                |     |-------2
        |  /                    |    /
        3-------------------8
'''


def fun(i,j,cost,m,l1):
    l.append(i)
    if(i==j):
        if cost<m:
            m=cost
            l1=l.copy()
        l.pop()
        return m,l1
    for i in d[i]:
        if(i[0] not in l):
            m,l1=fun(i[0],j,cost+i[1],m,l1)
    l.pop()
    return m,l1
d={5:[(7,1),(3,2)],7:[(5,1),(4,1),(3,2)],4:[(7,1),(8,4),(2,2)],8:[(3,4),(4,4),(2,3)],3:[(5,2),(7,3),(8,4)],2:[(4,2),(8,3)]}
l=[]
for i in d.keys():
    print(fun(5,i,0,99999,[]))