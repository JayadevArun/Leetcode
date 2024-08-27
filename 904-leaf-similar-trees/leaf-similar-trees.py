# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfsLeaf(self,root,l):
        if root is None:
            return
        if root.left is None and root.right is None:
            l.append(root.val)
        self.dfsLeaf(root.left,l)
        self.dfsLeaf(root.right,l)
        return l
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1=[]
        l2=[]
        l1=self.dfsLeaf(root1,l1)
        l2=self.dfsLeaf(root2,l2)
        return l1==l2