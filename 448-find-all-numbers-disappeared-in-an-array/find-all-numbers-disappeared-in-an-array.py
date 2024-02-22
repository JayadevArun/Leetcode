class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l=[]
        a=set(nums)
        for i in range(len(nums)):
            if i+1 not in a:
                l.append(i+1)
        return l

        # hm={}
        # h={}
        # for i in range(len(nums)):
        #     hm[i]=i+1
        #     if hm[i] not in list(set(nums)):
        #         h[i]=hm[i]
        # return list(h.values())