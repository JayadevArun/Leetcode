class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        ans=high
        while low<=high:
            mid=(low+high)//2
            hr=0
            for pile in piles:
                hr+=math.ceil(pile/mid)
            if hr<=h:
                ans=min(ans,mid)
                high=mid-1
            else:
                low=mid+1
        return ans