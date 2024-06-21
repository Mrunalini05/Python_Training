#360days in a year, 30days in a month, 6days in a week
#360    30     6
#ip:     65476
#op: ?y   ?m   ?w   ?d


n=int(input())
y=n//360
n=n%360
m=n//30
n=n%30
w=n//6
d=n%6
print(f"{y}:{m}:{w}:{d}")