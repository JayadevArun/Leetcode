class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n=sorted(nums)
        hm={}
        l=[]
        for i in range(len(n)):
            if n[i] not in hm:
                hm[n[i]]=i
        for i in nums:
            l.append(hm[i])
        return l

        # l=[]
        # for i in range(len(nums)):
        #     c=0
        #     for j in range(len(nums)):
        #         if nums[j]<nums[i]:
        #             c+=1
        #     l.append(c)
        # return l