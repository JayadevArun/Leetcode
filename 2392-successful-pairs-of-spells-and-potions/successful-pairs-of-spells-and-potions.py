class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int)->List[int]:
        res=[]
        potions.sort()
        lp=len(potions)
        for spell in spells:
            low,high=0,lp
            while low<high:
                mid=(low+high)//2
                if spell*potions[mid]>=success:
                    high=mid
                else:
                    low=mid+1
            if low==lp:
                res.append(0)
            else:
                res.append(lp-low)
        return res