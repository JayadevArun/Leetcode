# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return head
        if head.next is None:
            return head
        revHead=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return revHead

        # prev=None
        # cur=head
        # while cur:
        #     front=cur.next
        #     cur.next=prev
        #     prev=cur
        #     cur=front
        # return prev
