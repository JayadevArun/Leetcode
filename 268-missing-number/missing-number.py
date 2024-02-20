class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hm = {}
        for i in nums:
            hm[i] = i
        for i in range(len(nums)):
            if i not in hm:
                return i
        return len(nums)