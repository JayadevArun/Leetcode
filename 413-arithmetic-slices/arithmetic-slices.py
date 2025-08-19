class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        if n<3:
            return 0

        count=0
        left=0

        while left+2<n:
            diff=nums[left+1]-nums[left]
            right=left+2
            while right<n and diff==nums[right]-nums[right-1]:
                right+=1
                count+=1
            left+=1
        
        return count