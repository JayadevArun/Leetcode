class Solution:
    def hammingWeight(self, n: int) -> int:
        
        b=bin(n)[2:]
        l=list(b)
        return l.count("1")
