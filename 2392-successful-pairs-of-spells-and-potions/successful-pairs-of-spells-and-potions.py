class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int)->List[int]:
        res=[]
        potions.sort()
        lp=len(potions)
        for spell in spells:
            low,high=0,lp-1
            index=lp
            while low<=high:
                mid=(low+high)//2
                if spell*potions[mid]>=success:
                    high=mid-1
                    index=mid
                else:
                    low=mid+1
            res.append(lp-index)
        return res