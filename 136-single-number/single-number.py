class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        c=1
        for i in range(len(nums)):
            if len(nums)==1:
                return nums[0]
            elif nums[i]==nums[i+1]:
                c+=1
            elif nums[i]!=nums[i+1] and c==1:
                return nums[i]
            elif nums[i]!=nums[i+1] and c!=1:
                c=1
                if nums[i+1]==nums[-1]:
                    return nums[i+1]
                