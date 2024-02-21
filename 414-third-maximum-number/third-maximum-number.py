class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        t=sorted(list(set(nums)))
        return t[-1] if len(t)<3 else t[-3]