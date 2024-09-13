class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue=deque()
        rows=len(grid)
        cols=len(grid[0])
        time=0
        fresh=0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    queue.append([r,c])

        if fresh==0:
            return 0

        dir=[[0,1],[1,0],[0,-1],[-1,0]]
        while queue and fresh>0:
            for i in range(len(queue)):
                r,c=queue.popleft()
                for dr,dc in dir:
                    row=dr+r
                    col=dc+c
                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                        grid[row][col] = 2
                        queue.append([row, col])
                        fresh -= 1
            time+=1

        if fresh==0:
            return time
        else:
            return -1
