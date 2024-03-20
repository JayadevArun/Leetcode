class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c=0
        hm={}
        for i in jewels:
            hm[i]=1
        for j in stones:
            if j in hm:
                c+=1
        return c

        # c=0
        # for i in stones:
        #     if i in jewels:
        #         c+=1
        # return c