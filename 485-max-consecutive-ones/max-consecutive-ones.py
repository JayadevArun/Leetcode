class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        m=0
        for item in nums:
            if item==1:
                count+=1
            else:
                m=max(m,count)
                count=0
        return max(m,count)

        # c=0
        # l=0
        # for i in nums:
        #     if i==1:
        #         c+=1
        #         if c>l:
        #             l=c
        #     else:
        #         c=0
        # return l