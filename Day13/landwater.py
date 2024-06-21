#ip: 5
'''              0 1 0 0 1              1=land
                 1 0 0 1 1              0=water
                 0 0 0 0 0
                 1 0 0 0 0
                 1 0 0 0 1
'''
#op: 5----->the count of connected lands

#print the largest area of the connected lands
#op: 3


'''def rec(i,j,n,r):
    if r[i][j]==0:
        return
    r[i][j]=0
    if i > 0:
        rec(i-1,j,n,r)
    if j > 0:
        rec(i,j-1,n,r)
    if i<n-1:
        rec(i+1,j,n,r)
    if j<n-1:
        rec(i,j+1,n,r)
r=[[0,1,0,0,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,1]]
k=0
n=5
for i in range(n):
    for j in range(n):
        if r[i][j]==1:
            rec(i,j,0)
            k=k+1
print(k)'''

    #or
def fun(i,j,c):
    if(i<0 or j<0 or i>=n or j>=n or r[i][j]!=1):
        return c
    r[i][j]=2
    c=c+1
    c=fun(i,j-1,c)
    c=fun(i,j+1,c)
    c=fun(i-1,j,c)
    c=fun(i+1,j,c)
    return c
r=[[0,1,0,0,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,1]]
k=0
n=5
m=0
for i in range(n):
    for j in range(n):
        if r[i][j]==1:
            q=fun(i,j,0)
            if(q>m):
                m=q
            k=k+1
print(k,m)
