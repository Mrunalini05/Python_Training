#all 26 alphabets with space are there are not
#if there are special characters and numbers it doesn't work as a set
#ip: "the quick brown fox jumps over the lazy dog"
#op: yes

#ip: "qwweer yuiop asdfvgh JKL mnbvlkjcxz"
#op: no


#a="the quick brown fox jumps over the lazy dog"
b="abcdefghijklmnopqrstuvwxyz"   #b=97
a="qwweer yuiop asdfvgh JKL mnbvlkjcxz"
for i in b:                                         #for i in range(97orb,123):
    if(i not in a):                               #if(chr(i) not in a):
        print("no")
        break
else:
    print("yes")
    
    
#in dictionary
a=input()
d=[0]*26
for i in a:
    if(i.islower()):
        d[ord(i)-97]+=1                          #d[ord(i)-97=1
print(d)
print(all(d))                              