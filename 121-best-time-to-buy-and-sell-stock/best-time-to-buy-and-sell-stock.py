class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        c=0
        while r<len(prices):
            if prices[r]>prices[l]:
                p=prices[r]-prices[l]
                c=max(p,c)
            else:
                l=r
            r+=1
        return c

        # c=0
        # f=True
        # for i in range(len(prices)-1):
        #     if prices[i]>=prices[i+1]:
        #         continue
        #     else:
        #         f=False
        # if f==True:
        #     return 0
        # else:
        #     for i in range(len(prices)-1):
        #         for j in range(i+1,len(prices)):
        #             if prices[j]>prices[i]:
        #                 t=prices[j]-prices[i]
        #                 if t>c:
        #                     c=t
        #     return c
         
            