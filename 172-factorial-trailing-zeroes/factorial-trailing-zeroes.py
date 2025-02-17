class Solution:
    def trailingZeroes(self, n: int) -> int:
        c2=0
        c5=0
        for i in range(1,n+1):
            while i%2==0:
                c2+=1
                i//=2
            while i%5==0:
                c5+=1
                i//=5
        return min(c2,c5)