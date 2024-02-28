class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        c1=0
        c2=0
        for i in nums:
            c1+=i
        for i in nums:
            if len(str(i))==1:
                c2+=i
            else:
                for digit in str(i):
                    c2+=int(digit)
        return abs(c2-c1)
