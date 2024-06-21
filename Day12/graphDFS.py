#GRAPH: Depth first search(DFS)
#DFS- visit all the nodes by the path
'''
        5---------7--------4
        |          /            |    \
        |      /                |     |-------2
        |  /                    |    /
        3-------------------8

'''
#op: [5, 7, 4, 8, 2]
def fun(i):
    l.append(i)
    for i in d[i]:
        if(i not in l):
            fun(i)
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
fun(5)
print(l)