class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = {}
        c = 0
        for num in nums:
            if k-num in d and d[k-num] > 0:
                d[k-num] -= 1
                c += 1
            else:
                if num in d:
                    d[num] += 1
                else:
                    d[num] = 1
        return c