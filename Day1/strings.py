'''ip: aaabbaaaaddd
op:a3b2a4d3'''

s="aaabbaaaaddd"
a=' '
count=1
for i in range(len(s)-1):
    if(s[i]==s[i+1]):
        count=count+1
    else:
        a=a+s[i]+str(count)
        count=1
a=a+s[i]+str(count)
print(a)