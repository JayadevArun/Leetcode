class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hm={}
        c=0
        for i in nums:
            if i in hm:
                c+=hm[i]
                hm[i]+=1
            else:
                hm[i]=1
        return c

        # count = {}
        # result = 0
        # for num in nums:
        #     if num in count:
        #         result += count[num]
        #         count[num] += 1
        #     else:
        #         count[num] = 1
        # return result

        # c=0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             c+=1
        # return c