#ip: heights of the building=[3,5,9,6,8,10]
#at morning 6am: sunlight falls on building 3,5,9,10 (6,8 are hide from the 9)
#at evening 6pm: sunset falls on the building 10 only
#op: 4 1


#arr=[3,5,9,6,8,10]
arr=[3,4,5,10,3,4]
l=[0]*len(arr)
r=[0]*len(arr)
m=0
c=0
for i in range(len(arr)):
    if(arr[i]>m):
        m=arr[i]
        c=c+1
    l[i]=m
m1=0
c1=0
for i in range(len(arr)-1,-1,-1):
    if(arr[i]>m1):
        m1=arr[i]
        c1=c1+1
    r[i]=m1
print(c,c1)