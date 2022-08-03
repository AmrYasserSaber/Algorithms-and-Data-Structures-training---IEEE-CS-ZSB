# https://leetcode.com/problems/palindromic-substrings/     <--- like of the problem
def palindromic(s):
    rev = ''.join(reversed(s))
    if (s == rev):
        return True
    return False
s=input()
l=list(s)
c=0
for i in range (len(s)):
    for j in range(len(s)):
        if i>j:
            continue
        if i==j:
            c+=1
            continue
        if palindromic(s[i:j+1]):
            c+=1
print(c)


# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         def palindromic(s):
#             rev = ''.join(reversed(s))
#             if (s == rev):
#                 return True
#             return False
#         c=0
#         for i in range (len(s)):
#             for j in range(len(s)):
#                 if i>j:
#                     continue
#                 if i==j:
#                     c+=1
#                     continue
#                 if palindromic(s[i:j+1]):
#                     c+=1
#         return(c)   