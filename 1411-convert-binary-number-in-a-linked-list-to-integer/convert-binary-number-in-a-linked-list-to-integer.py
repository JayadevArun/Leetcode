# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        value=""
        cur=head
        while cur:
            value+=str(cur.val)
            cur=cur.next
        return int(value, 2)

        # value=0
        # cur=head
        # while cur:
        #     value=value*2+cur.val
        #     cur=cur.next
        # return value
