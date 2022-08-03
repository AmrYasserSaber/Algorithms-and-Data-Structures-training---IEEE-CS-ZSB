# https://leetcode.com/problems/climbing-stairs/       <--- like of the problem
def fib(n):
    one,two =1,1
    for i in range(n-1):
        temp=one
        one=one+two
        two=temp
    return one
n=int(input())
print(fib(n))

#the slotion in the link  -->


#class Solution(object):
    #def climbStairs(self, n):
        #one,two =1,1
        #for i in range(n-1):
            #temp=one
            #one=one+two
            #two=temp
        #return one