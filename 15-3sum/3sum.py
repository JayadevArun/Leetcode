class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sums=0
        res=[]
        ss=set()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if s==sums:
                    ss.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif s<sums:
                    j+=1
                else:
                    k-=1
        res=list(ss)
        return res