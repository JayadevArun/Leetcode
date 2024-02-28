class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        c=0
        hm={}
        for i in nums:
            if i not in hm:
                hm[i]=1
            else:
                hm[i]+=1
        for i in hm:
            if i+k in hm:
                c+=hm[i]*hm[i+k]
        return c

        # c=0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if abs(nums[j]-nums[i])==k:
        #             c+=1
        # return c