# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a,b,n = 0,0,0
        h = head
        while h:
            n += 1
            if n == k:
                a = h.val
            h = h.next
        h = head
        c = 0
        while h:
            c += 1
            if n-c+1 == k:
                b = h.val
                h.val = a
            h = h.next
        h = head
        c = 0
        while h:
            c += 1
            if c == k:
                h.val = b
            h = h.next
        return head