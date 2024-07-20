# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(node: Optional[TreeNode], values: List[int]):
            if not node:
                return
            inorder(node.left, values)
            values.append(node.val)
            inorder(node.right, values)
        l=[]
        inorder(root,l)
        dif=float('inf')
        for i in range(1,len(l)):
            dif=min(dif,l[i]-l[i-1])
        return dif
        