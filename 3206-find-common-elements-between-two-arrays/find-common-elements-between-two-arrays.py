class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=set(nums1)
        b=set(nums2)
        c1=0
        c2=0
        for i in nums1:
            if i in b:
                c1+=1
        for i in nums2:
            if i in a:
                c2+=1
        return [c1,c2]