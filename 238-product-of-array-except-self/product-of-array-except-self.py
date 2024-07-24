class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l=len(nums)
        result=[0]*l

        preprod=1
        for i in range(l):
            result[i]=preprod
            preprod*=nums[i]

        postprod=1
        for i in range(l-1,-1,-1):
            result[i]*=postprod
            postprod*=nums[i]

        return result