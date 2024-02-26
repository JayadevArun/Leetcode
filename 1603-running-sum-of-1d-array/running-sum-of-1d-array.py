class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l=[]
        c=0
        for i in range(len(nums)):
            c+=nums[i]
            l.append(c)
        return l