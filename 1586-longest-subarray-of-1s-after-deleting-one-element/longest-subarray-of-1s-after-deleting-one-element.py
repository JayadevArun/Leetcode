class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res=0
        l=0
        zero=0
        for r in range(len(nums)):
            zero+=1 if nums[r]==0 else 0
            while zero>1:
                zero-=1 if nums[l]==0 else 0
                l+=1
            res=max(res,r-l)
        return res