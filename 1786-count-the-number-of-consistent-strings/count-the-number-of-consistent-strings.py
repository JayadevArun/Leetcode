class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        l=list(allowed)
        count=len(words)
        for i in words:
            for j in i:
                if j not in l:
                    count-=1
                    break
        return count
        
        # l=list(allowed)
        # a=[]
        # c=0
        # for item in words:
        #     for i in item:
        #         f=True
        #         if i not in l:
        #             f=False
        #             break
        #     if f==True:
        #         c+=1
        # return c