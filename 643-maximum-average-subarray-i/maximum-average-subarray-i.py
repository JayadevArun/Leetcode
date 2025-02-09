class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums)<k:
            return 0
        s=sum(nums[:k])
        m=s
        for i in range(k,len(nums)):
            s+=nums[i]-nums[i-k]
            m=max(m,s)
        return m/k
