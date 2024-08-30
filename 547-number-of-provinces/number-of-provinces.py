class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(c):
            visited.add(c)
            for n in range(l):
                if isConnected[c][n]==1 and n not in visited:
                    dfs(n)
        visited=set()
        l=len(isConnected)
        count=0
        for city in range(l):
            if city not in visited:
                dfs(city)
                count+=1
        return count