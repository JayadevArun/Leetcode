class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        sums=0
        mini=float("inf")
        for r in range(len(nums)):
            sums+=nums[r]
            while sums>=target:
                mini=min(mini,r-l+1)
                sums-=nums[l]
                l+=1
        if mini==float("inf"):
            return 0
        else:
            return mini