class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l=len(nums)

        prefix=[1]*l
        postfix=[1]*l
        result=[0]*l

        for i in range(1,l):
            prefix[i]=prefix[i-1]*nums[i-1]

        for i in range(l-2,-1,-1):
            postfix[i]=postfix[i+1]*nums[i+1]

        for i in range(l):
            result[i]=prefix[i]*postfix[i]

        return result