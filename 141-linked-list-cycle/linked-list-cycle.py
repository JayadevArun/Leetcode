# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f=head
        while f and f.next:
            head=head.next
            f=f.next.next
            if f==head:
                return True
        return False