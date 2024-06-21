#ip: school
#     3
#     L 2  ----> hoolsc
#     R 3 ----> oolsch
#     L 1  ----> chools
#take frst char from each rotation: hoc
#possible subsequence from the input: sch, cho, hoo, ool
#sort all the subsequence to get anagram equal to hoc--->jumple the word
#if hoc is a anagram of any subsequence then print: yes, if not no
#op: yes  ---> hoc is an anagram of cho.




a=input()
n=int(input())
#str=''
str=[]
for i in range(n):
    b=input()
    if b[0]=='L':
        #str+=a[int(b[2])]
        str.append(a[int(b[2])])
    else:
        #str+=a[-int(b[2])]
        str.append(a[-int(b[2])])
print(str)
#str=list(str)
str.sort()
b=[]
for i in range(len(a)-n+1):
    t=sorted(list(a[i:n+i]))
    b.append(t)
print(b)
print(str)
for i in b:
    if(i==str):
        print("yes")
        break
else:
    print("no")