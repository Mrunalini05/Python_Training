#DP
#ip: [1,3,4,5]---coins
#      17
#op: 4

#in Tabulation
#subtract the value from the listnumber and add the value which is stored already in the table +1(which is removed)
#and update the value checking the min(current,up) and then update it
'''
          0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
    1    0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
    3    0 1 2 1 2 3 2 3 4 3  4   5   4    5   6   5   6  7
    4    0 1 2 1 1 2 2 2 2 3  3   3   3    4   4   4   4  5
    5    0 1 2 1 1 1 2 2 2 2  2   3   3    3   3   3   4  5
'''

#ip: [3,4]
#      6
#if there is a -1or negative value in current row and up keep it as it is,if there is -1 in current row and value at up keep the value,
#if not if value is there in the current row then value+1 and check the added value with up value which is minimum updated it, if up value is -1 then keep the added value
'''
                0 1 2 3 4 5 6
              -1-1-1-1-1-1-1
        3     0-1-1 1 -1-1 2
        4     0-1-1 1  1-1 2
        
        [0,-1,-1,1,1,-1,2]
'''
#op: 2


def fun():
    l1=[-1]*(n+1)
    l1[0]=0
    for i in l:
        for j in range(1,n+1):
            if(j>=i):
                if(l1[j-i]!=-1):
                    if(l1[j]!=-1):
                        l1[j]=min(l1[j],l1[j-i]+1)
                    else:
                        l1[j]=l1[j-i]+1
    print(l1[-1])
l=[3,4]
n=5
#l=[1,3,4,5]
#n=17    
fun()