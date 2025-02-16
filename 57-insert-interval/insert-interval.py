class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        c=0
        n=len(intervals)
        while c<n and intervals[c][1]<newInterval[0]:
            res.append(intervals[c])
            c+=1
        while c<n and intervals[c][0]<=newInterval[1]:
            newInterval[0]=min(newInterval[0],intervals[c][0])
            newInterval[1]=max(newInterval[1],intervals[c][1])
            c+=1
        res.append(newInterval)  
        while c<n:
            res.append(intervals[c])
            c+=1
        return res