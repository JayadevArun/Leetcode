class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l=[]
        m=max(candies)
        for num in candies:
            if num+extraCandies>=m:
                l.append(True)
            else:
                l.append(False)
        return l