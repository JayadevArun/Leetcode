class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        l=''
        c=0
        for i in s:
            if i==' ':
                c+=1
            if c==k:
                break
            l+=i
        return l