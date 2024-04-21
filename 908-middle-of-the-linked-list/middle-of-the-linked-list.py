# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur=head
        size=0
        i=0
        while cur!=None:
            size+=1
            cur=cur.next
        index=size//2
        cur=head
        while cur!=None:
            if i==index:
                return cur
            else:
                cur=cur.next
                i+=1

        # back=front=head
        # while front and front.next:
        #     back=back.next
        #     front=front.next.next
        # return back
