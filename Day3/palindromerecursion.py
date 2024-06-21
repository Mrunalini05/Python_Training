#ip: 12321
#reverse the number and check whether it is a palindrome or not
#op: palindrome

'''n=int(input())
rev=0
t=n
while t>0:
    r=t%10
    rev=(rev*10)+r
    t=t//10
print(rev)
if(rev==n):
    print("palindrome")
else:
    print("not palindrome")
'''


def reverse(n,rev):
    if n == 0:
        return rev
    else:
        r = n % 10
        rev = (rev * 10) + r
        return reverse(n//10,rev)

n = int(input())
if(n==reverse(n,0)):
    print("palindrome")
else:
    print("not palindrome")
