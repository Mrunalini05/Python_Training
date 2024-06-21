#ip: 6
#      0 1 1 1 0 1
#      0 1 0 1 0 0
#      1 0 0 1 0 0
#      0 0 0 1 1 1
#      1 1 0 0 0 1
#      1 1 1 0 1 0
#      4 6---->tree has caught the fire and it burns left,right,up and down
#op: 8---->unburnt trees


'''def fun(i,j):
    if(i<0 or j<0 or i>=n or j>=n or m[i][j]!=1):
        return
    if(m[i][j]==1):
        m[i][j]=2
    fun(i-1,j)
    fun(i,j-1)
    fun(i+1,j)
    fun(i,j+1)
    return

n=int(input())
i=int(input())
j=int(input())
m=[]
for i in range(n):
    n=list(map(int, input().strip().split()))
    m.append(n)

for row in m:
    print(row)

fun(i,j)
c=0
for i in range(n):
    for j in range(n):
        if(m[i][j]==1):
            c=c+1
print(c)
'''



def rec(i,j,n,r):
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
r=[[0,1,1,1,0,1],[0,1,0,1,0,0],[1,0,1,1,0,0],[0,0,0,1,1,1],[1,1,0,0,0,1],[1,1,1,0,1,0]]
k=0
n=6
a=int(input())
b=int(input())
rec(a,b,n,r)
for i in range(n):
    for j in range(n):
        if r[i][j]==1:
            k=k+1
print(k)
