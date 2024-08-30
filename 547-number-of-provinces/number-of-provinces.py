class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(c):
            visited.add(c)
            for n in range(len(isConnected[c])):
                if isConnected[c][n]==1 and n not in visited:
                    dfs(n)
        visited=set()
        count=0
        for city in range(len(isConnected)):
            if city not in visited:
                dfs(city)
                count+=1
        return count