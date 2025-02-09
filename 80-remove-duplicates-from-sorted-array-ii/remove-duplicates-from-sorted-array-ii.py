class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        c=1
        res=1
        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                c=1
                nums[res]=nums[i]
                res+=1
            else:
                c+=1
                if c<=2:
                    nums[res]=nums[i]
                    res+=1
        return res
            
