class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n==0:
            return 0
        res=0
        while n>=5:
            n=n//5
            res+=n
        return res 