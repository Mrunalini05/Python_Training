'''l1=[2,5,7,9]
l2=[1,3,6,7,10,13]
l=l1+l2
l.sort()
print(l)'''


l1=[2,5,7,9]
l2=[1,3,6,7,10,13]
l=[]
i=0
j=0
while i<len(l1) and j<len(l2):
    if l1[i]<l2[j]:
        l.append(l1[i])
        i+=1
    else:
        l.append(l2[j])
        j+=1
if j<len(l2):
    l.append(l2[j])
if i<len(l1):
    l.append(l1[i])
    
'''if j<len(l2):
    l.extend(l2[j:])
if i<len(l1):
    l.extend(l1[i:])'''
print(l)
