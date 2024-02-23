class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        for i in set(nums1):
            if i in set(nums2):
                l.append(i)
        return l