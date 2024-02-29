class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        l=list(allowed)
        a=[]
        c=0
        
        for item in words:
            
            for i in item:
                f=True
                if i not in l:
                    f=False
                    break
            if f==True:
                c+=1
        return c


