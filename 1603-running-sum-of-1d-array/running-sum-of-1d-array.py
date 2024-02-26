class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l=[nums[0]]
        c=nums[0]
        for i in range(1,len(nums)):
            c+=nums[i]
            l.append(c)
        return l

        # l=[]
        # c=0
        # for i in range(len(nums)):
        #     c+=nums[i]
        #     l.append(c)
        # return l