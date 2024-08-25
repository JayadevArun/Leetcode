class Solution:
    def rob(self, nums: List[int]) -> int: 
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        sum1=nums[0]
        sum2=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            s=max(sum1+nums[i],sum2)
            sum1=sum2
            sum2=s
        return max(sum1,sum2)
