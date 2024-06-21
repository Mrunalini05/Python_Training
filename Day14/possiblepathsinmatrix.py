#print all the possible paths from starting point to ending point
#ip: 4x3
'''
#op:  - - - -
         - - - -
         - - - -
'''


'''def fun(i,j,m,n,c):
    if(i<0 or i>=n or j<0 or j>=m):
        return c
    if(i==n-1 and j==m-1):
        c=c+1
        return c
    vi.append((i,j))
    if((i-1,j) not in vi):
        c=fun(i-1,j,m,n,c)
    if((i,j-1) not in vi):
        c=fun(i,j-1,m,n,c)
    if((i+1,j) not in vi):
        c=fun(i+1,j,m,n,c)
    if((i,j+1) not in vi):
        c=fun(i,j+1,m,n,c)
    vi.pop()
    return c
n=3
m=4
vi=[]
print(fun(0,0,m,n,0))
'''




#obstacle at a position
def fun(i,j,c):
    if(i<0 or i>=n or j<0 or j>=m or (i==k and j==l)):
        return c
    if(i==n-1 and j==m-1):
        c=c+1
        return c
    vi.append((i,j))
    if((i-1,j) not in vi):
        c=fun(i-1,j,c)
    if((i,j-1) not in vi):
        c=fun(i,j-1,c)
    if((i+1,j) not in vi):
        c=fun(i+1,j,c)
    if((i,j+1) not in vi):
        c=fun(i,j+1,c)
    vi.pop()
    return c
n=3
m=4
k=1
l=2
vi=[]
print(fun(0,0,0))