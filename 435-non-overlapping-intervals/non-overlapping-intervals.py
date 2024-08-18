class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[1])
        check=intervals[0][1]
        count=0
        for l in range(1,len(intervals)):
            if intervals[l][0]<check:
                count+=1
            else:
                check=intervals[l][1]
        return count