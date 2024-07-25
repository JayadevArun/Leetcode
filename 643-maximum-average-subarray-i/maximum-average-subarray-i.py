class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        s = 0
        m = float('-inf') 
        avg = 0   

        for i in range(len(nums)):
            s += nums[i]
            if i - l + 1 == k: 
                avg = s / k
                m = max(m, avg)
                s -= nums[l]
                l += 1

        return m
