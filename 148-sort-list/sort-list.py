# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        l=head
        r=self.fetchMid(head)
        temp=r.next
        r.next=None
        r=temp

        l=self.sortList(l)
        r=self.sortList(r)
        
        return self.mergeList(l,r)

    def fetchMid(self,head):

        s=head
        f=head.next

        while f and f.next:
            s=s.next
            f=f.next.next

        return s

    def mergeList(self,l,r):

        node = ListNode()
        tail = node

        while l and r:
            if l.val < r.val:
                tail.next = l
                l = l.next
            else:
                tail.next = r
                r = r.next
            tail = tail.next

        if l:
            tail.next = l
        elif r:
            tail.next = r

        return node.next