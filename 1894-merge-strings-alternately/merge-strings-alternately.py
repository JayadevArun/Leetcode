class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        i=0
        j=0
        l1=len(word1)
        l2=len(word2)
        while i<l1 or j<l2:
            if i<l1:
                s+=word1[i]
            if j<l2:
                s+=word2[j]
            i+=1
            j+=1
        return s