class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s)==0:
            return True
        if len(t)==0:
            return False
        
        for letter in s:
            if letter not in t:
                return False
        
        si=0
        ti=0

        while ti<len(t):
            if s[si]==t[ti]:
                si+=1
                if si==len(s):
                    return True
            ti+=1
        return False