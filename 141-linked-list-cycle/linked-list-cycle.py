# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s=set()
        node=head
        while node:
            if node in s:
                return True
            s.add(node)
            node=node.next
        return False