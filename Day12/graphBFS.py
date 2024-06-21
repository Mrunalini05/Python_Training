#GRAPH: Breadth First Search(BFS)
#BFS- it visits all the nodes in the graph without following the path
'''     5---------7--------4
        |          /            |    \
        |      /                |     |-------2
        |  /                    |    /
        3-------------------8
'''
#op: v=[5,7,3,4,8,2]

def fun(i):
    q.append(i)
    while q!=[]:
        for i in d[q[0]]:
            if(i not in q and i not in v):
                q.append(i)
        v.append(q.pop(0))
        #print(v[-1])
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
q=[]
v=[]
fun(5)
print(v)