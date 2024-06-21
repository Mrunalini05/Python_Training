#ip:[2,3,5,6]
#    11
#should take the single coins to get the given value
# 2- 5,6
#op: yes

'''
         0 1 2 3 4 5 6 7 8 9 10 11
    2   1 0 1 0 0 0 0 0 0 0   0   0
    3   1 0 1 1 0 1 0 0 0 0   0   0
    5   1 0 1 1 0 1 0 1 1 0   1   0
    6   1 0 1 1 0 1 1 1 1 1   1   1
'''

def can_make_target(coins, target):
    # Initialize the dp array with False and set dp[0] to True
    dp = [0] * (target + 1)
    dp[0] = 1

    # Iterate over each coin
    for i in coins:
        # Update the dp array from back to front
        for j in range(target, i - 1, -1):
            if dp[j - i]:
                dp[j] = 1

    return dp[target]

# Example usage
coins = [2, 3, 5, 6]
target_value = 11
result = can_make_target(coins, target_value)

if result==1:
    print("yes")
else:
    print("no")
