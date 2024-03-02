class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        c=0
        hm={}
        for i in words:
            rev=i[::-1]
            if rev in hm:
                c+=1
                del hm[rev]
            else:
                hm[i]=1
        return c

        # c=0
        # for i in range (len(words)):
        #     for j in range(i+1,len(words)):
        #         if words[i]==words[j][::-1]:
        #             c+=1
        # return c