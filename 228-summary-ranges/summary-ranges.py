class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result=[]
        i=0
        n=len(nums)
        while i<n:
            start=nums[i]
            while i<n-1 and nums[i]+1==nums[i+1]:
                i+=1
            end=nums[i]
            if start!=end:
                result.append(str(start)+'->'+str(end))
            else:
                result.append(str(end))
            i+=1
        return result