# https://leetcode.com/problems/coin-change/       <--- like of the problem

class Solution:
    def coinChange(self,coins, amount: int) -> int:
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for a in range (1,amount+1):
            for c in coins:
                if a-c >=0:
                    dp[a]=min(dp[a],1+dp[a-c])
        return (dp[amount]) if dp[amount]!= amount+1 else -1













































# underdevolved solution
# def coinChange(self,v, C: int) -> int:
#     def greedy(l,cap):
#         res=0
#         if cap==1 and 1 in l:
#             return 1
#         elif cap==0:
#             return 0
#         elif cap==1 and 1 not in l or len(l)==0 or cap<min(l):
#             return -1
#         else : 
#             res= cap//l[0]
#             w=greedy(l[1:],cap-res*l[0])
#             if w==-1:
#                 return -1
#             else:
#                 return(res+w)
#     v.sort()
#     if C==0 :
#         return(0)
#     if  C%v[len(v)-1]==0 :
#         return(C//v[len(v)-1])
#     if len(v)==1 and v[0]!=C :
#         return(-1)
#     n=len(v)
#     t=[[-1 for i in range(C + 1)] for j in range(1,n + 2)]
#     for i in range(0,n+1):
#         if i == 0 :
#                 continue
#         for j in range (0,C+1):
#             if j==0:
#                 continue
#             m=v[:i]
#             m.reverse()
#             temp=greedy(m,j)
#             if (t[i-1][j]==-1) or (temp<=t[i-1][j]):
#                 t[i][j]=temp
#             else:
#                 t[i][j]=t[i-1][j]     
#     return(t[n][C])

