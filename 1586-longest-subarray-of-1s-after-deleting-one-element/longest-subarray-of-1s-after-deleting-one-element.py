class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res=0
        l=0
        zero=0
        for r in range(len(nums)):
            if nums[r]==0:
                zero+=1
            else:
                zero+=0
            while zero>1:
                if nums[l]==0:
                    zero-=1
                else:
                    zero-=0
                l+=1
            res=max(res,r-l)
        return res