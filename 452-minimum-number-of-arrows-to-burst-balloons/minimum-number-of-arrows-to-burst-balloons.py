class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        arrows=1
        check=points[0][1]
        for l in range(1,len(points)):
            if points[l][0]>check:
                arrows+=1
                check=points[l][1]
        return arrows