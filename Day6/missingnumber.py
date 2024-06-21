#268- leetcode
#find the missing number
#ip:7
#    0 5 3 6 7 2 1
#op: 4
'''n=int(input())
l=[0, 5, 3, 6, 7, 2, 1]
a=[]
for i in range(n+1):
    a.append(i)
    if(i not in l):
        print(i)
'''        

n=int(input())  
l=list(map(int,input().split(' ')))      
a=sum(l)
n=(n*(n+1))//2
print(n-a)