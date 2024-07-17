class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda i:i[0])

        merge=[]

        for interval in intervals:
            if not merge or merge[-1][1]<interval[0]:
                merge.append(interval)
            else:
                merge[-1][1]=max(merge[-1][1],interval[1])
        return merge
