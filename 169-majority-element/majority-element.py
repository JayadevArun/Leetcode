class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        c = 0
        l = len(nums)
        if l==1:
            return nums[0]
        for i in range(l):
            if nums[i] in hm:
                hm[nums[i]] += 1
                if hm[nums[i]] > l/2:
                    return nums[i]
            else:
                hm[nums[i]] = 1