class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=0
        c=nums.count(0)
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[k]=nums[i]
                k+=1 
        for i in range(len(nums)-c,len(nums)):
            nums[i]=0

        # k=0
        # c=0
        # for i in range(len(nums)):
        #     if nums[i]==0:
        #         c+=1
        #     else:
        #         nums[k]=nums[i]
        #         k+=1
        # for i in range(len(nums)-c,len(nums)):
        #     nums[i]=0

        # c=nums.count(0)
        # for i in range(c):
        #     nums.remove(0)
        # for i in range(c):
        #     nums.append(0)