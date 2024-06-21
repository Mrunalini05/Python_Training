#ip: [2,5,2,3,6,7,1,0,5,7]
'''
                        
                     |
                   ||      |
             |    ||    | |
             |    ||    | |
             |  |||    | |
           ||||||    | |
           |||||||  | |
    l=  2555677777
    r=  7777777777
'''
#op: 20

arr=[2,5,2,3,6,7,1,0,5,7]
l=[0]*len(arr)
r=[0]*len(arr)
m=0
for i in range(len(arr)):
    if(arr[i]>m):
        m=arr[i]
    l[i]=m
m1=0
for i in range(len(arr)-1,-1,-1):
    if(arr[i]>m1):
        m1=arr[i]
    r[i]=m1
s=0
for i in range(len(arr)):
    s=s+abs(min(l[i],r[i])-arr[i])
print(s)


#leetcode
'''def trap(height,res):
    if not height:
        return True
    l=0
    r=len(height)-1
    maxl=height[l]
    maxr=height[r]
    while l<r:
        if maxl<maxr:
            l+=1
            maxl=max(maxl,height[l])
            res+=maxl-height[l]
        else:
            r-=1
            maxr=max(maxr,height[r])
            res+=maxr-height[r]
    return res
height=[2,5,2,3,6,7,1,0,5,7]
print(trap(height,0))'''