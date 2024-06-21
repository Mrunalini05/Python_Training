#169-leetcode
#print the occurrence of the number and half the length of the list which is greater.
#ip: [4,8,2,4,4,8,4]   l=7
#      l//2=3
#      4 occured=4times
#      8 occured=2times
#op: 4 wins
'''l=[4,8,2,4,4,8,4]
c=0
m=0
p=l[0]
for i in range(1,len(l)):
    if(c(l[i])>m):
        m=c(l[i])
        p=l[i]
print(m, p)
'''

#a=[1,1,1,2,2,2,2]
a=[4,8,2,4,4,8,4]
c=1
p=a[0]                 #winnerperson
for i in range(1,len(a)):
    if(a[i]==p):
        c=c+1
    else:
        c=c-1
        if(c==0):
            c=c+1
            p=a[i]
print(p)