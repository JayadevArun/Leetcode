class Solution:
    def maxArea(self, height: List[int]) -> int:
        result=0
        l=0
        r=len(height)-1
        while l<r:
            ar=(r-l)*min(height[l],height[r])
            result=max(result,ar)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return result

        # BruteForce-Time Exceeded
        # result=0
        # for l in range(len(height)):
        #     for r in range(l+1,len(height)):
        #         ar=(r-l)*min(height[l],height[r])
        #         result=max(result,ar)
        # return result