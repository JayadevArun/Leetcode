class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def BS(nums,target,leftshift):
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
            
        l=BS(nums,target,True)
        r=BS(nums,target,False)
        return [l,r]