class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        l=[]
        l.append(0)
        num=0
        for i in gain:
            num+=i
            l.append(num)
        return max(l)