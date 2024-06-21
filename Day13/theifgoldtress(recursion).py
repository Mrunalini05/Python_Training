#ip: [13,9,4,10,5,7]
# there is thief who want to grab the gold from the above houses
# the condition is if the theif is at 1st house then he should not go to next house, he can go other than that.
#op: 30  ---->13+10+7

'''                                                                           [13,9,4,10,5,7]    s=30
                                                                                   /             \
                                                          s=30 13,[4,10,5,7]          s=26  9,[10,5,7]
                                                                         /          \                         /        \
                                                        s=11 4,[5,7]  s=17 10,[7]    s=17 10,[7]   s=5 5,[]
                                                                     /   \                /  \                /   \
                                                                  5,[]  7,[]         7,[]  []           7,[]   []
'''



def fun(l):
    if(len(l)==0):
        return 0
    if(len(l)==1):
        return l[0]
    if(len(l)==2):
        return max(l)
    le=l[0]+fun(l[2:])
    ri=l[1]+fun(l[3:])
    return max(le,ri)
l=[13,9,4,10,5,7]
print(fun(l))