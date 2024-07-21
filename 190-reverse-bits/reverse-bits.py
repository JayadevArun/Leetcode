class Solution:
    def reverseBits(self, n: int) -> int:
        binstr = bin(n)[2:].zfill(32)
        revstr = binstr[::-1]
        revint = int(revstr, 2)
        return revint