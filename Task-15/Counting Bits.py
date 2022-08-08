# https://leetcode.com/problems/counting-bits/      <--- like of the problem
class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        def hammingWeight(self,n: int) -> int:
            res =0
            while n:
                res += n%2
                n=n>>1
            return res
        for i in range(n+1):
            l.append(hammingWeight(0,i))
        return(l)