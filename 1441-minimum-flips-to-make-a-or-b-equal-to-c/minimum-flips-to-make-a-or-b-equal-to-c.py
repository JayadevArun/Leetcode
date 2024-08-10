class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count=0
        while a>0 or b>0 or c>0:
            if (a&1 and b&1) and not c&1:
                count+=2
            elif (not a&1 and not b&1) and c&1:
                count+=1
            elif ((a&1 and not b&1) or (not a&1 and b&1))  and not c&1:
                count+=1
            a>>=1
            b>>=1
            c>>=1
        return count