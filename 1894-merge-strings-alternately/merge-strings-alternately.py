class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        i=0
        j=0
        l1=len(word1)
        l2=len(word2)
        while i<l1 and j<l2:
            s+=word1[i]
            s+=word2[j]
            i+=1
            j+=1
        if j<l2:
            s+=word2[j:]
        if i<l1:
            s+=word1[i:] 
        
        return s