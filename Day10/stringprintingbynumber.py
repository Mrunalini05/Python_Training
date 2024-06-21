#ip: "hello:5438,car:214,book:8799,apple:2187"
#hello length is=4, then in numbers if there is 4 the print the char of the 4 in hello it is-o
#car length=3 if number is not there then take next small number that is 2-a if not print x
#op: oaxp



s=input().split(',')
r=''
for i in s:
    b=i.split(":")
    print(b[0],b[1])
    w=len(b[0])
    print(w,b[1])
    if str(w) in b[1]:
        r+=b[0][-1]
    else:
        for i in range(w-1,0,-1):
            if str(i) in b[1]:
                r+=b[0][i-1]
                break
        else:
            r+='x'
print("".join(r))