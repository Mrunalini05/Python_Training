#find the longest substring without repeating characters
#ip: abfgresagtyuiofde
#from a we count the numbers until it reaches any repeated letter from that we count the values from nxt index
#a-7, b-7, f-6, g-5, r-12, e-10, s-11......
#longest subtring is: resagtyuiofd-12

s=input()
d={}
s1=""
i=0
m=0
while(i<len(s)):
        if(s[i] not in s1):
            s1+=s[i]
            d[s[i]]=i
        else:
            if(len(s1)>m):
                m=len(s1)
            s1=""
            i=d[s[i]]
        i=i+1
print(m)