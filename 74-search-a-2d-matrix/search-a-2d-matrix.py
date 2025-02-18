class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row=len(matrix)
        col=len(matrix[0])
        left=0
        right=(row*col)-1
        while left<=right:
            mid=(left+right)//2
            midval=matrix[mid//col][mid%col]
            if midval==target:
                return True
            elif midval<target:
                left=mid+1
            else:
                right=mid-1
        return False