class Solution:
    def isHappy(self, n: int) -> bool:
        hm = {}
        while n != 1:
            if n in hm:
                return False
            hm[n] = 0
            n = sum(int(i) ** 2 for i in str(n))
        return True
            