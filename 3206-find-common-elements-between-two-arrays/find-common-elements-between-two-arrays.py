class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1=0
        c2=0
        l=[]
        for i in nums1:
            if i in nums2:
                c1+=1
        l.append(c1)
        for i in nums2:
            if i in nums1:
                c2+=1
        l.append(c2)
        return l