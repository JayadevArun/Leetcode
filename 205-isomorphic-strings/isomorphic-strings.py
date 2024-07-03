class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False  

        hm={}
        ss=set()

        for letterS,letterT in zip(s,t):
            if letterS in hm:
                if hm[letterS]!=letterT:
                    return False
            else:
                if letterT in ss:
                    return False
                hm[letterS]=letterT
                ss.add(letterT)
        return True