class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = {}
        c = 0
        for num in nums:
            t=k-num
            if t in d and d[t] > 0:
                d[t] -= 1
                c += 1
            else:
                if num in d:
                    d[num] += 1
                else:
                    d[num] = 1
        return c