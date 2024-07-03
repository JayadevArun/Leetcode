class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        hms = {}
        hmt = {}

        for letterS, letterT in zip(s, t):
            if letterS in hms:
                if hms[letterS] != letterT:
                    return False
            else:
                hms[letterS] = letterT
            
            if letterT in hmt:
                if hmt[letterT] != letterS:
                    return False
            else:
                hmt[letterT] = letterS

        return True    