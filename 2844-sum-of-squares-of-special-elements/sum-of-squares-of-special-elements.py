class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        c=0
        for i in range(len(nums)):
            if n%(i+1)==0:
                c+=nums[i]*nums[i]
        return c