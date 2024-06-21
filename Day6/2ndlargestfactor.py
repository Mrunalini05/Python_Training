#print second largest factor
#n=12, key=2
# 1,2,3,4,6,12
#op: 6


'''def KthLargestFactor(N, K):
    for i in range(N+1,0,-1):
        if N % i == 0:
            K -= 1
        if K == 0:
            return i
    return -1
N = 12
K = 2
print(KthLargestFactor(N, K))'''


N = 12
K = 2
for i in range(N+1,0,-1):
    if N % i == 0:
        K -= 1
    if K == 0:
        print(i)