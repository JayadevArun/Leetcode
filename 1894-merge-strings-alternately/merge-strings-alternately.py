class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=[]
        i,j=0,0
        l1=len(word1)
        l2=len(word2)
        while i<l1 or j<l2:
            if i<l1:
                l.append(word1[i])
            if j<l2:
                l.append(word2[j])
            i+=1
            j+=1
        return ''.join(l)