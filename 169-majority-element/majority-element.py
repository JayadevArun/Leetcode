class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        c = 0
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)):
            if nums[i] in hm:
                hm[nums[i]] += 1
                if hm[nums[i]] > len(nums)/2:
                    return nums[i]
            else:
                hm[nums[i]] = 1