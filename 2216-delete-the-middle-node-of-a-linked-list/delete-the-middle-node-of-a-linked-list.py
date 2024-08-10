# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return None
        
        l=0
        cur=head
        while cur:
            l+=1
            cur=cur.next

        mid=l//2
        cur=head
        prev=None
        for i in range(mid):
            prev=cur
            cur=cur.next
        
        prev.next=cur.next

        return head

