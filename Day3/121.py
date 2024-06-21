#ip: 15 3 2 7 8 4
#      m  t w t f s
#op: 6
#ip:  5 3 2 7 8 4
#      m t w t f s
#op: 6
#ip: 5 4 2 9 7 1
#     m t w t f s
#op: 7
#ip: 9 8 7 6 5 4
#      m t w t f s
#op: 6

prices=[15, 3, 2, 8, 1, 4, 9]
pr=0
buy=prices[0]
for i in range(len(prices)):
    if prices[i]<buy:
        buy=prices[i]
    elif prices[i]-buy>pr:
        pr=prices[i]-buy
print(pr)