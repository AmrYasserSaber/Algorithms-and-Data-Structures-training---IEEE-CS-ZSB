# https://leetcode.com/problems/reverse-bits/     <--- like of the problem

def reverseBits(self, n: int) -> int:
        res=0
        for i in range(32):
            bit = (n>>i)&1
            res=res | (bit<<(31-i))
        return(res)
n=int(input())
print(reverseBits(0,n))


# class Solution:
#     def reverseBits(self, n: int) -> int:
#         res=0
#         for i in range(32):
#             bit = (n>>i)&1
#             res=res | (bit<<(31-i))
#         return(res)