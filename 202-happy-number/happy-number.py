class Solution:
    def isHappy(self, n: int) -> bool:
        hm={}
        while True:
            n = sum(int(i) ** 2 for i in str(n))
            if n==1:
                return True
            elif n in hm:
                return False
            else:
                hm[n]=0
            