# https://leetcode.com/problems/product-of-array-except-self/submissions/   <--- like of the problem




class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res







# def productExceptSelf(self, nums):
#         m=1
#         res=[]
#         t=False
#         if 0 in nums:
#             n=nums.index(0)
#             nums[n]=1
#             t=True
#         for i in nums:
#             m=i*m
#         if t:
#             l=[0]*len(nums)
#             l[n]=m
#             return (l)
#         for i in nums:
#             res.append(m//i)
#         return(res)