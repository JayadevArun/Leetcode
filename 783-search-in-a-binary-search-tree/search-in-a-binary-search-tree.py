# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        node=root
        while node:
            if node.val==val:
                return node
            elif val<node.val:
                node=node.left
            elif val>node.val:
                node=node.right                
        return node