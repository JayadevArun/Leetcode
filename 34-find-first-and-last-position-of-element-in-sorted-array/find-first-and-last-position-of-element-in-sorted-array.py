class Solution:
    def BS(self,nums,target,leftshift):
        l,r=0,len(nums)-1
        i=-1
        while l<=r:
            m=(l+r)//2
            if nums[m]>target:
                r=m-1
            elif nums[m]<target:
                l=m+1
            else:
                i=m
                if leftshift:
                    r=m-1
                else:
                    l=m+1
        return i
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=self.BS(nums,target,True)
        r=self.BS(nums,target,False)
        return [l,r]