#stack in leetcodeques
s="leet**cod*e"
stack=[]
for i in s:
    if i=='*':
        stack.pop()
    else:
        stack.append(i)
print(''.join(stack))