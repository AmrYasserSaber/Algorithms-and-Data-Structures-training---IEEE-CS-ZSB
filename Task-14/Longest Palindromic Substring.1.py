# https://leetcode.com/problems/longest-palindromic-substring/     <--- like of the problem
def palindromic(s):
    rev = ''.join(reversed(s))
    if (s == rev):
        return True
    return False
s=input()
l=list(s)
table=[]
longest=0
start=0
end=0
for i in range (len(s)):
    temp=[0]*len(s)
    table.append(temp)
    for j in range(len(s)):
        if i>j:
            continue
        if i==j:
            table[i][j]=1
            continue
        if palindromic(s[i:j+1]):
            table[i][j]=1
            if j-i>longest:
                longest=j-i
                start=i
                end=j
print(s[start:end+1])


#class Solution:
#    def longestPalindrome(self, s: str) -> str:
#        def palindromic(s):
#            rev = ''.join(reversed(s))
#            if (s == rev):
#                return True
#            return False
#        l=list(s)
#        table=[]
#        longest=0
#        start=0
#        end=0
#        for i in range (len(s)):
#            temp=[0]*len(s)
#            table.append(temp)
#            for j in range(len(s)):
#                if i>j:
#                    continue
#                if i==j:
#                    table[i][j]=1
#                if palindromic(s[i:j+1]):
#                    table[i][j]=1
#                    if j-i>longest:
#                        longest=j-i
#                        start=i
#                        end=j
#        return(s[start:end+1])