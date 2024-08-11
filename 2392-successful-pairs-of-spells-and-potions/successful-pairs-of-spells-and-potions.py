class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int)->List[int]:
        res=[]
        potions.sort()
        for spell in spells:
            low=0
            high=len(potions)-1
            index=len(potions)
            while low<=high:
                mid=(low+high)//2
                if spell*potions[mid]>=success:
                    high=mid-1
                    index=mid
                else:
                    low=mid+1
            res.append(len(potions)-index)
        return res