# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,m):
            if node is None:
                return 0
            count=1 if node.val>=m else 0
            m=max(m,node.val)
            count+=dfs(node.left,m)
            count+=dfs(node.right,m)
            return count
        return dfs(root,root.val)