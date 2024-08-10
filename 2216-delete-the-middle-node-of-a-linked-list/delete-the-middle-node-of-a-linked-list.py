# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return None

        one=head
        two=head
        prev=None
        while two and two.next:
            prev=one
            one=one.next
            two=two.next.next
        if prev:
            prev.next=one.next

        return head
