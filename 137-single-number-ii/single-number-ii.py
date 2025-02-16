class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hm={}
        for num in nums:
            hm[num]=hm.get(num,0)+1
        for k,v in hm.items():
            if v==1:
                return k