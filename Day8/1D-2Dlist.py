#convert the following list into 2D list
#make the less rows
#each row should contain distinct elements
#all the 2D elements should contain all the 1D list
#ip: [1,2,3,4,1,2,3,1,2]
#op: [[1 2 3 4],[1 2 3],[1 2]]
#     1 2 3 4
#     1 2 3
#     1 2

#ip: [2,3,1,3,4,3,2]
#op: [[2 3 1 4],[3 2],[3]]
#      2 3 1 4
#      3 2
#      3

#ip: [4,5,2,1]
#op: [[4 5 2 1]]

#in dictionary:
#[2,3,1,3,4,3,2]
#[2:2,3:3,1:1,4:1]
#make them until '0'


'''l=list(map(int,input().split(',')))
r=[]
row=[]
for i in l:
    if i not in row:
        row.append(i)
    else:
        r.append(row)
        row=[i]
if row!=[]:
    r.append(row)
print(r)
'''



l=list(map(int,input().split(',')))
r=[]
c=0
while(c!=len(l)):
    row=[]
    for i in range(len(l)):
        if(not str(l[i]).isalpha()):
            if(l[i] not in row):
                c=c+1
                row.append(l[i])
                l[i]='a'
    r.append(row)
print(r)



#in dictionary
l=list(map(int,input().split(',')))                                   
d={}
r=[]
c=0
for i in l:
    if(i not in d):
        d[i]=1
    else:
        d[i]=d[i]+1
while(c!=len(l)):
    row=[]
    for i in d:
        if(d[i]!=0):
            d[i]=d[i-1]
            c=c+1
            row.append(i)
    r.append(row)
print(r)