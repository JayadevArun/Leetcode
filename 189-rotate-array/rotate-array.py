class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        l=len(nums)-k
        a=nums[:l]
        nums[:l]=[]
        nums.extend(a)
        return nums