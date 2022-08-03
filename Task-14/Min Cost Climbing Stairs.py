# https://leetcode.com/problems/min-cost-climbing-stairs/      <--- like of the problem

def minCostClimbingStairs(self, cost) -> int:
    n=len(cost)
    cost.append(0)
    cost.append(0)
    for i in range(n,-1,-1):
        if i ==n:
            continue
        cost[i]=cost[i] + min(cost[i + 1], cost[i + 2])
    return (min(cost[0],cost[1]))
l=list(map(int,input().split()))
print(minCostClimbingStairs(0,l))

#the slotion in the link  -->

# class Solution:
#     def minCostClimbingStairs(self, cost) -> int:
#         n=len(cost)
#         cost.append(0)
#         cost.append(0)
#         for i in range(n,-1,-1):
#             if i ==n:
#                 continue
#             cost[i]=cost[i] + min(cost[i + 1], cost[i + 2])
#         return (min(cost[0],cost[1]))