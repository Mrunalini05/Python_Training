#ip: khoor       #d
#     3              #5
#op: hello       #y          #3steps back for each alphabet

'''str=input()
num=int(input())
def fun(str,num):
    res=" "
    for i in str:
            s=ord('a')
            res+=chr((ord(i)-s-num)%26+s)
    return res
print(fun(str,num))
'''

a='bvec'
b=4
c=b%26
d=''
for i in a:
    if((ord(i)-c)>=97):
        d+=chr(ord(i)-c)
    else:
        d+=chr((ord(i)-c)+26)
print(d)