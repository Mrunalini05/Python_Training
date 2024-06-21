#find the longest common subsequence- DP
#ip: abcd         abcd
#     axbdc        axbdc
#op: abc-3  or   abd
#if the string is same then add 1 with the diagonalof upleft, if not max(upof prev and leftof present)
#in Tabulation
'''              a      b       c      d
            0   0      0       0      0
        a  0   1      1       1      1
        x  0   1      1       1      1
        b  0   1      2       2      2
        d  0   1      2       2      3
        c  0   1      2       3      3
'''

s1=input()
s2=input()
s=""
n=len(s2)+1
u=len(s1)
v=len(s2)
m=[]
for i in range(len(s1)+1):
    l=[0]*n
    m.append(l)
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if(s1[i-1]==s2[j-1]):
            m[i][j]=m[i-1][j-1]+1
        else:
            m[i][j]=max(m[i][j-1],m[i-1][j])
print(m[len(s1)][len(s2)])
while u!=0 and v!=0:
    if(s1[u-1]==s2[v-1]):
        s=s+s1[u-1]
        u=u-1
        v=v-1
    else:
        if(m[u][v]==m[u-1][v]):                             #if(m[u][v]==m[u][v-1]): 
            u=u-1                                                              #v=v-1
        else:                                                          #else: 
             v=v-1                                                             #u=u-1   #op: abc
print(s[::-1])