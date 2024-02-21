class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        nums=list(set(nums))
        nums.sort()
        c=0
        if len(nums)<3:
            return nums[-1]
        for i in range(len(nums)-1,-1,-1):
            if nums[i]!=nums[i-1]:
                c+=1
                if c==2:
                    return nums[i-1]

