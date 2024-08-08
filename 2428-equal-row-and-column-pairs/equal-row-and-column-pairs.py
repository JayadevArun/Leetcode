class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        l=len(grid)
        hm={}
        count=0
        for r in grid:
            rt=tuple(r)
            if rt in hm:
                hm[rt]+=1
            else:
                hm[rt]=1
        for i in range(l):
                ct=tuple(grid[j][i] for j in range(l))
                if ct in hm:
                    count+=hm[ct]
        return count