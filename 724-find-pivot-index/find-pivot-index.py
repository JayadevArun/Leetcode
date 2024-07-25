class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totsum=sum(nums)
        lsum=0
        for i in range(len(nums)):
            rsum=totsum-nums[i]-lsum
            if rsum==lsum:
                return i
            lsum+=nums[i]
        return -1