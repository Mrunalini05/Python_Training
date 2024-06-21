key="the quick brown fox jumps over the lazy dog"
message="vkbs bs t suepuv"
a=''#'abcdefghijklmnopqrstuvwxyz'
r=''
for i in key:
    if(i not in r and i!=' '):
        r+=i
for i in message:
    if(i!=' '):
        a=a+chr(r.index(i)+97)
    else:
        a=a+' '
print(a)