# https://leetcode.com/problems/single-number/       <--- like of the problem
nums=[2,2,1]
nums.sort()
n=len(nums)
for i in range (n):
    if n==1:
        print (nums[0])
        quit()
    if i==0 and nums[i+1]!=nums[0]:
        print(nums[0])
        quit()
    elif i==0 :
        continue
    if nums[i]==nums[i-1]:
        continue
    if i == n-1:
        print(nums[i])
        quit()
    if nums[i]!=nums[i+1]:
        print(nums[i])
        quit()





# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         n=len(nums)
#         for i in range (n):
#             if n==1:
#                 return (nums[0])
#             if i==0 and nums[i+1]!=nums[0]:
#                 return(nums[0])
#             elif i==0 :
#                 continue
#             if nums[i]==nums[i-1]:
#                 continue
#             if i == n-1:
#                 return(nums[i])
#             if nums[i]!=nums[i+1]:
#                 return(nums[i])