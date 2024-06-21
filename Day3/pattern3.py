#ip: 5 or 7
#op: 4
#        1 1 1 1 1 1 1
#        1 2 2 2 2 2 1
#        1 2 3 3 3 2 1
#        1 2 3 4 3 2 1
#        1 2 3 3 3 2 1
#        1 2 2 3 2 2 1
#        1 2 2 2 2 2 1
#        1 1 1 1 1 1 1


n=int(input())
k=1
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
           print('1 ', end='')
        elif i==1 or i==n-2 or j==1 or j==n-2:
           print('2 ', end='')
        elif i==2 or i==n-3 or j==2 or j==n-3:
           print('3 ', end='')
        elif i==3 or i==n-4 or j==3 or j==n-4:
           print('4 ', end='')
    print()