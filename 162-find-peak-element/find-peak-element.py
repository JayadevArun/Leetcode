class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        nums = [float('-inf')] + nums + [float('-inf')]
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i+1] and nums[i]>nums[i-1]:
                return i-1