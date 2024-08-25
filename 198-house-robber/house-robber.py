class Solution:
    def rob(self, nums: List[int]) -> int:
        sum1=0
        sum2=0
        for num in nums:
            s=max(sum1+num,sum2)
            sum1=sum2
            sum2=s
        return sum2
