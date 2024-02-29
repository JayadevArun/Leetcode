class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        count=0
        m=0
        for item in gain:
            count+=item
            m=max(count,m)
        return m

        # l=[]
        # l.append(0)
        # num=0
        # for i in gain:
        #     num+=i
        #     l.append(num)
        # return max(l)