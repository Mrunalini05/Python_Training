#swapping and sorting
#ip: [4,9,8,2,14,3,5,6]
# 4 8 9 2 14 3 5 6
#    2 8 9 14 3 5 6
#       8 9 14 3 5 6
#          3  9 14 5 6
#              5  9 14 6
#                  6  9 14
#op: 4 2 8 3 5 6 9 14
l=[4,9,8,2,14,3,5,6]
a=[]
for i in range(len(l)-2):
    if(l[i]>l[i+1]):
        l[i],l[i+1]=l[i+1],l[i]
    if(l[i+1]>l[i+2]):
        l[i+1],l[i+2]=l[i+2],l[i+1]
    if(l[i]>l[i+1]):
        l[i],l[i+1]=l[i+1],l[i]
print(l)