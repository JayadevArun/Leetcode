class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i in range(len(nums)):
            hash[i]=nums[i]
        for i in range(len(nums)):
            rem=target-nums[i]
            if rem in hash.values() and nums.index(rem)!=i:
                return [i,nums.index(rem)]