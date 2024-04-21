# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        sum=0
        arr=[root]
        while arr:
            n=arr.pop()
            if n:
                if low<=n.val<=high:
                    sum+=n.val
                if n.val>low:
                    arr.append(n.left)
                if n.val<high:
                    arr.append(n.right)
        return sum

        # if not root:
        #     return 0
        # if root.val<low:
        #     return self.rangeSumBST(root.right,low,high)
        # elif root.val>high:
        #     return self.rangeSumBST(root.left,low,high)
        # return root.val+self.rangeSumBST(root.right,low,high)+self.rangeSumBST(root.left,low,high)

        # if not root:
        #     return 0
        # if low<=root.val<=high:
        #     sum=root.val
        # else:
        #     sum=0
        # lsum=self.rangeSumBST(root.left,low,high)
        # rsum=self.rangeSumBST(root.right,low,high)
        # return sum+lsum+rsum
