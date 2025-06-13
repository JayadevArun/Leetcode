class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indeg=[0]*numCourses
        g=[[] for i in range(numCourses)]

        for a,b in prerequisites:
            g[b].append(a)
            indeg[a]+=1

        q=deque()
        for i in range(numCourses):
            if indeg[i]==0:
                q.append(i)

        count=0
        while q:
            c=q.popleft()
            count+=1
            for n in g[c]:
                indeg[n]-=1
                if indeg[n]==0:
                    q.append(n)
        
        return count==numCourses