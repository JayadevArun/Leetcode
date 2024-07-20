# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        sum={}
        count={}
        def dfs(node,h):
            if not node:
                return
            if h not in sum:
                sum[h] = node.val
                count[h] = 1
            else:
                sum[h] += node.val
                count[h] += 1
            dfs(node.left,h+1)
            dfs(node.right,h+1)
        dfs(root,0)
        l=[]
        for i in range(len(count)):
            l.append(sum[i]/count[i])
        return l
