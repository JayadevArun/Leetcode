class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        l = [0] * (n + 1)
        for i in range(1, n + 1):
            l[i] = bin(i).count('1')
        return l
