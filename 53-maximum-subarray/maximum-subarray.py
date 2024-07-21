class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxim=nums[0]
        sum=nums[0]
        for i in nums[1:]:
            sum=max(sum+i,i)
            maxim=max(maxim,sum)
        return maxim