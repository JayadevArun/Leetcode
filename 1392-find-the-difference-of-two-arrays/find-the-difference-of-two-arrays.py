class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hm1 = {}
        hm2 = {}

        for num in nums1:
            hm1[num] = True
        for num in nums2:
            hm2[num] = True
        
        res1 = {num for num in hm1 if num not in hm2}
        res2 = {num for num in hm2 if num not in hm1}
        
        return [list(res1), list(res2)]