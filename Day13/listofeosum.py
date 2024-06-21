#l1=[6,3,2,9,4,7]
#l2=[8,7,5,3,6,9]
#add the even number in l1 to all the odd numbers in the l2
#op: [13,11,9,15,9,7,5,11,11,9,7,13]

def fun(i,j,l1,l2,r):
    for i in l1:
        if(i%2==0):
            for j in l2:
                if(j%2!=0):
                    r.append(i+j)
                    j=j+1
            i=i+1
    return r
            

l1=[6,3,2,9,4,7]
l2=[8,7,5,3,6,9]
print(fun(0,0,l1,l2,[]))


#in recursion

def fun(i,j,l1,l2,r):
    if i>=len(l1):
        return r
    if j>=len(l2):
        return fun(i+1,0,l1,l2,r)
    if l1[i]%2==0 and l2[j]%2!=0:
            r.append(l1[i]+l2[j])
    return fun(i,j+1,l1,l2,r)
            

l1=[6,3,2,9,4,7]
l2=[8,7,5,3,6,9]
print(fun(0,0,l1,l2,[]))


#print in the sets in recursion
#l1=[6,3,2,9,4,7]
#l2=[8,7,5,3,6,9]
#add the even number in l1 to all the odd numbers in the l2
#op: [(13,11,9,15), (9,7,5,11), (11,9,7,13)]

