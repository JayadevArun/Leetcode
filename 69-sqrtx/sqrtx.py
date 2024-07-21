class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        for i in range(2,x//2+2):
            if i*i==x:
                return i
            elif i*i>x:
                return i-1