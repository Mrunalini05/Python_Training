#ip: 2
#      polikujmnhytgbvfredcxswqaz        #lecksographical order
#      abcd ->sort the order by the above given alphabetic order input
#op: bdca
#      qwryupcsfoghjkldezxvbintma
#      ativedoc
#op: codevita


n=int(input())
while(n):
    a=input()
    c=input()
    s=''
    for i in a:
        if(i in c):
            s=s+(i*c.count(i))
    print(s)
    n=n-1