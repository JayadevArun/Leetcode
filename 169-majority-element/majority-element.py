class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        c=1
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                c+=1
                if c>len(nums)/2:
                    return nums[i]
            elif nums[i]!=nums[i+1]:
                if c>len(nums)/2:
                    return nums[i]
                else:
                    c=1