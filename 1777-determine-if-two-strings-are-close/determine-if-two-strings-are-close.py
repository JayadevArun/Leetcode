class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        l1=[]
        l2=[]
        s1=set(word1)
        s2=set(word2)
        if s1!=s2:
            return False
        for c in s1:
            l1.append(word1.count(c))
        for c in s2:
            l2.append(word2.count(c))
        l1.sort()
        l2.sort()
        return l1==l2