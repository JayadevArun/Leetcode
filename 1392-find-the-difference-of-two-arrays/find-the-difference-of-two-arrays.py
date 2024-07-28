class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)

        l1, l2 = s1 - s2, s2 - s1
        
        return [list(l1), list(l2)]