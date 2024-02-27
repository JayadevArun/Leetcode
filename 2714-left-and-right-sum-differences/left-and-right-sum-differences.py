class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left=0
        res=[]
        right=sum(nums)
        for item in nums:
            left+=item
            res.append(abs(left-right))
            right-=item
        return res

        # l=[]
        # r=[]
        # c1=0
        # c2=0
        # res=[]
        # for i in range(len(nums)):
        #     l.append(c1)
        #     c1+=nums[i]
        # for i in range(len(nums)-1,-1,-1):
        #     r.append(c2)
        #     c2+=nums[i]
        # r.reverse()
        # for i in range(len(nums)):
        #     n=abs(l[i]-r[i])
        #     res.append(n)
        # return res