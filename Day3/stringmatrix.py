#ip: 3                                                    #ip: 4
#     xyz                                                 #     abcd
#     pqr                                                 #     xyze                          
#     abc                                                #      pqrw
#     "yraxpazr"                                     #      stuv
#op: no                                                #      "cyptdzsayq"
                                                            #op: no


'''n = int(input())
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        ele= input()
        row.append(ele)
    matrix.append(row)
s=input()
print("The entered matrix is:")
for row in matrix:
    print(row)
'''
#for row by row
'''n=int(input())
m=[]
for i in range(n):
    m.append(input())
s=input()
f=0
for i in range(len(s)):
    if(s[i] in m[i%n]):                                           
        continue
    else:
        f=1
        break
if(f==1):
    print("no")
else:
    print("yes")
'''

'''n=int(input())
m=[]
for i in range(n):
    m.append(input())
s=input()
for i in range(len(s)):
    if(s[i] not in m[i%n]):
        print("no")
        break
else:
    print("yes")
'''
#no repetations and should be row by row
n=int(input())
m=[]
for i in range(n):
    m.append(list(input()))
s=input()
f=0
for i in range(len(s)):
    if(s[i] not in m[i%n]):
        print("no")
        f=1
        break
    else:
        m[i%n].remove(s[i])
if(f==0):
    print("yes")