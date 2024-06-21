#find two numbers are co-prime or not
'''import math
a=5
b=10print()
'''

a=int(input())
b=int(input())
for i in range(2,(min(a,b)//2)+1):
    if a%i==0 and b%i==0:
        print("no")
        break
else:
    print("yes")