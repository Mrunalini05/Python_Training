'''class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):                                                                  #slicing-more time complexity
            ans.append(abs(sum(nums[:i])-sum(nums[i+1:])))
        return ans'''
    

n=[4,7,5,2,3]
s=sum(n)
x=0
r=[]
for i in n:
    r.append(abs((x)-(s-i-x)))
    x=x+i
print(r)


'''n=[4,7,5,2,3]
s=sum(n)
x=0
j=0
for i in n:
    n[j]=abs((x)-(s-i-x))
    x=x+i
    j=j+1
print(n)
'''