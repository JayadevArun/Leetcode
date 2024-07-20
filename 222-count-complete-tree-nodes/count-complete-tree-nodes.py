# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def leftHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    def rightHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        lh = self.leftHeight(root)
        rh = self.rightHeight(root)
        
        if lh == rh:
            return (1 << lh) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)