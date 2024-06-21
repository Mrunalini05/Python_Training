#if not palindrome print next nearest palindrome
#ip: 121
#op: palindrome

#ip: 122
#op: 131

#ip: 1234
#divide the string into equal halfs: 12  34
#mirror for the frst number is: 1221
#1221<1234 then,
#increment the second number: 1321
#halfs is: 13 21
#mirror it: 1331
#1331<1234, false (for even number)
#op: 1331

#ip: 24
#op: 33

#ip:1112
#op: 1221

#ip: 7654
#op: 7667

#ip: 56472
#56 472 (mirror 56)
#56465<56472 then
#increment middle element and mirror the frst two elements
#56565
#op: 56565

#ip:76583
#op:76667


'''def is_palindrome(num):
    return str(num) == str(num)[::-1]
def next_greatest_palindrome(num):
    num += 1
    while not is_palindrome(num):
        num += 1
    return num
n = int(input("Enter a number: "))
next_palindrome = next_greatest_palindrome(n)
print(f"The next greatest palindrome after {n} is {next_palindrome}.")'''



n=1112
s=str(n)
l=len(s)
if l%2!=0:
    f = s[:l//2 + 1]
    l_part = s[(l//2) + 1:]
    x = s[:l//2]
    if int(l_part) >= int(x):
        f = str(int(f) + 1)
        f = f + f[:l//2][::-1]
        print(f)
    else:
        f = f + f[:l//2][::-1]
        print(f)
else:
    f = s[:l//2]
    l_part = s[l//2:]
    if int(f[::-1]) > int(l_part):
        f = f + f[::-1]
        print(f)
    else:
        while True:
            f = str(int(f[-1]) + 1)
            if int(f[::-1]) > int(l_part):
                f = f + f[::-1]
                print(f)
                break