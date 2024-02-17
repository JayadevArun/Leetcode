class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        result=False
        for i in range(len(nums)):
            if target==nums[i]:
                return i
                result=True
            else:
                continue
        if result==False:
            for i in range(len(nums)):
                if nums[i]>target:
                    return i
                else:
                    if nums[-1]<target:
                        return len(nums)
