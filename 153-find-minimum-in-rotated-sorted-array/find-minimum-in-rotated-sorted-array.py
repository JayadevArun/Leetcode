class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        res=nums[0]
        while left<=right:
            if nums[left]<nums[right]:
                res=min(res,nums[left])
                break
            mid=(left+right)//2
            res=min(res,nums[mid])
            if nums[mid]>=nums[right]:
                left=mid+1
            elif nums[mid]<nums[right]:
                right=mid-1
        return res