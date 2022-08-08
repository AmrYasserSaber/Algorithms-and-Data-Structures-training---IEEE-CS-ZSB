# https://leetcode.com/problems/missing-number/submissions/    <--- like of the problem

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range (max(nums)+2):
            if i not in nums:
                return (i)