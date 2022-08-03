# https://leetcode.com/problems/house-robber/      <--- like of the problem

l=list(map(int,input().split()))
def robing(l):
    n=len(l)
    if n==0:
        return 0
    if n==1:
        return l[0]
    if n==2:
        return max(l[0],l[1])
    dp=[0]*n
    dp[0]=l[0]
    dp[1]=max(l[0],l[1])
    for i in range(2,n):
        dp[i]=max(dp[i-1],dp[i-2]+l[i])
    return dp[n-1]
print(robing(l))

#the slotion in the link  -->

# class Solution:
#     def rob(self,l):
#         n=len(l)
#         if n==0:
#             return 0
#         if n==1:
#             return l[0]
#         if n==2:
#             return max(l[0],l[1])
#         dp=[0]*n
#         dp[0]=l[0]
#         dp[1]=max(l[0],l[1])
#         for i in range(2,n):
#             dp[i]=max(dp[i-1],dp[i-2]+l[i])
#         return dp[n-1]
        


