class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm1={}
        hm2={}
        c1=0
        c2=0
        for i in nums1:
            hm1[i]=hm1.get(i,0)+1
        for i in nums2:
            hm2[i]=hm2.get(i,0)+1
        for i,f1 in hm1.items():
            if i in hm2:
                c1+=f1
        for i,f2 in hm2.items():
            if i in hm1:
                c2+=f2
        return [c1,c2]

        # a=set(nums1)
        # b=set(nums2)
        # c1=0
        # c2=0
        # for i in nums1:
        #     if i in b:
        #         c1+=1
        # for i in nums2:
        #     if i in a:
        #         c2+=1
        # return [c1,c2]