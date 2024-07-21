# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = head
        res = []

        while cur:
            res.append(cur.val)
            cur = cur.next

        cur = head
        res.sort()
        
        for i in res:
            cur.val = i
            cur = cur.next
            if not cur:
                break

        return head