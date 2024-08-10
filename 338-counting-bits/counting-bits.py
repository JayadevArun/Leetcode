class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(n+1):
            n=bin(i).count('1')
            l.append(n)
        return l