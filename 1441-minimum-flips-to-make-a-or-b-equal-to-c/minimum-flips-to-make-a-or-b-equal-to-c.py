class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        n = 0
        while c > 0 or b > 0 or a > 0:
            if c&1 == 1:
                if a&1 == 0 and b&1 == 0:
                    n += 1
            else:
                if a&1 == 1 and b&1 == 1:
                    n += 2
                elif a&1 == 1 or b&1 == 1:
                    n += 1
            b >>= 1
            a >>= 1
            c >>= 1
        return n