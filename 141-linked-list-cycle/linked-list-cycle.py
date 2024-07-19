# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hm={}
        node=head
        while node:
            if node in hm:
                return True
            hm[node]=1
            node=node.next
        return False