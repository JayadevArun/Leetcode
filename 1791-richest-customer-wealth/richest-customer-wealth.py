class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res=0
        for item in accounts:
            res=max(res,sum(item))
        return res       

        # m=s=0
        # for item in accounts:
        #     s=sum(item)
        #     m=max(s,m)
        # return m

        # t=0
        # for i in accounts:
        #     c=0
        #     for j in i:
        #         c+=j
        #     if c>t:
        #         t=c
        # return t      
