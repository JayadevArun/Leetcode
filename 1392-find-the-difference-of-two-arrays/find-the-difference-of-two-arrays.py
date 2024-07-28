class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l1=[]
        l2=[]
        for a in nums1:
            if a not in nums2 and a not in l1:
                l1.append(a)
        for b in nums2:
            if b not in nums1 and b not in l2:
                l2.append(b)
        return [l1,l2]