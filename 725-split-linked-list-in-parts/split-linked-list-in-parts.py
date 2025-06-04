# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        l=0
        cur=head
        while cur:
            cur=cur.next
            l+=1

        partsize=l//k
        ex=l%k

        res=[]
        curr=head
        for i in range(k):
            phead=curr
            if i<ex:
                newpartsize=partsize+1
            else:
                newpartsize=partsize

            for j in range(newpartsize-1):
                curr=curr.next

            if curr:
                newpart=curr.next
                curr.next=None
                curr=newpart

            res.append(phead)
        
        return res
