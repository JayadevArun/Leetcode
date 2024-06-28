class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si=0
        if(len(s)==0):
            return True
        for letter in t:
            if si<len(s) and letter==s[si]:
                si+=1
            if si==len(s):
                return True
        return False