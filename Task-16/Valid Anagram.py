# https://leetcode.com/problems/valid-anagram/    <--- like of the problem

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listS=list(s)
        listT=list(t)
        if len(listS) != len(listT):
            return(False)
        for i in listS:
            if i in listT:
                listT.remove(i)
            else:
                return(False)
        return(True)