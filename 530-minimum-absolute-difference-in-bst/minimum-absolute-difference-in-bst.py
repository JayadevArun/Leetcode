# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(node: Optional[TreeNode], l: List[int]):
            if not node:
                return
            inorder(node.left, l)
            l.append(node.val)
            inorder(node.right, l)
        l=[]
        inorder(root,l)
        dif=99999999
        for i in range(1,len(l)):
            dif=min(dif,l[i]-l[i-1])
        return dif
        