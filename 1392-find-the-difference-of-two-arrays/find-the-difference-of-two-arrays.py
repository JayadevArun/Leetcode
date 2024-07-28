class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hm1 = {}
        hm2 = {}
        for num in nums1:
            if num not in hm1:
                hm1[num] = 0
            hm1[num] += 1
        for num in nums2:
            if num not in hm2:
                hm2[num] = 0
            hm2[num] += 1
        l1 = []
        for num in hm1:
            if num not in hm2:
                l1.append(num)
        l2 = []
        for num in hm2:
            if num not in hm1:
                l2.append(num)
        return [l1, l2]