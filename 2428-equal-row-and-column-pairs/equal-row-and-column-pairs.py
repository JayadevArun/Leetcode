class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hm={}
        count=0
        for r in grid:
            rt=tuple(r)
            if rt in hm:
                hm[rt]+=1
            else:
                hm[rt]=1
        for c in zip(*grid):
                ct=tuple(c)
                if ct in hm:
                    count+=hm[ct]
        return count