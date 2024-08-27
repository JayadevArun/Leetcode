# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node,m):
        if node is None:
            return 0
        if node.val>=m:
            count=1
        else:
            count=0
        m=max(m,node.val)
        count+=self.dfs(node.left,m)
        count+=self.dfs(node.right,m)
        return count
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root,root.val)