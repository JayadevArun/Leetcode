class Solution:
    def climbStairs(self, n: int) -> int:
        a=1
        b=1
        for i in range(2,n+1):
            t=b
            b=a+b
            a=t
        return b