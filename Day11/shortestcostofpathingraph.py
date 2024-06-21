#print the shortest cost for the given graph from 5to2

              #1        #1
'''     5---------7--------4
        |          /            |    \#2
#2    |      /  #3          |#4 |-------2
        |  /                    |    /#3
        3-------------------8
'''                  #4

def fun(i,j,cost,m):
    l.append(i)
    if(i==j):
        if cost<m:
            m=cost
        l.pop()
        return m
    for n,w in d[i]:
        if(n not in l):
            m=fun(n,j,cost+w,m)
    l.pop()
    return m
d={5:[(7,1),(3,2)],7:[(5,1),(4,1),(3,2)],4:[(7,1),(8,4),(2,2)],8:[(3,4),(4,4),(2,3)],3:[(5,2),(7,3),(8,4)],2:[(4,2),(8,3)]}
l=[]
print(fun(5,2,0,99999))
