class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=len(nums)
        nums.sort()
        for i in range(l):
            if nums[i]!=i:
                return i
        return l