#print the pair of 3 possible combinations
l=[3,2,5,4,1,6,8]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            print(l[i],l[j],l[k])


#in recursion
def combination(l,k):
    def fun(curr,start):
        if len(curr)==k:
            print(curr)
            return
        for i in range(start,len(l)):
            fun(curr+[l[i]],i+1)
        return
    fun([],0)
l=[3,5,1,6]
k=3
combination(l,k)