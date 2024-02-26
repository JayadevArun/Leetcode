class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a=[]
        b=[]
        c=[]
        for i in range(n):
            a.append(nums[i])
        for i in range(n,2*n):
            b.append(nums[i])
        for i in range(n):
            c.append(a[i])
            c.append(b[i])
        return c