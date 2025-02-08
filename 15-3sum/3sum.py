class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sums=0
        res=[]
        ss=set()
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if s==sums:
                    t=(nums[i],nums[j],nums[k])
                    ss.add(t)
                    j+=1
                    k-=1
                elif s<sums:
                    j+=1
                else:
                    k-=1
        res=list(ss)
        return res