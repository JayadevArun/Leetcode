class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hm={}
        count=0
        for r in grid:
            if tuple(r) in hm:
                hm[tuple(r)]+=1
            else:
                hm[tuple(r)]=1
        for i in range(len(grid)):
                ct=tuple(grid[j][i] for j in range(len(grid)))
                if ct in hm:
                    count+=hm[ct]
        return count