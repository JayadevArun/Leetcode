class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hm={}
        c=0
        for i in range(len(nums)):
            if nums[i] not in hm:
                
                hm[nums[i]]=1
                nums[c]=nums[i]
                c+=1
                
        return c
