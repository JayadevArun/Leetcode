class NumArray:

    def __init__(self, nums: List[int]):
        self.arr=[]
        sums=0
        for n in nums:
            sums+=n
            self.arr.append(sums)

    def sumRange(self, left: int, right: int) -> int:
        r=self.arr[right]
        if left!=0:
            l=self.arr[left-1]
        else:
            l=0
        return r-l


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)