class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left==0:
            return 0
        if left==right:
            return left
        if len(bin(left))!=len(bin(right)):
            return 0
        while right>left:
            right &=(right-1)
        return right
        