# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, c: Optional[ListNode], d: Optional[ListNode]) -> Optional[ListNode]:
        a=b = ListNode()
        while c and d:
            if c.val < d.val:
                b.next = c
                b = b.next
                c = c.next
            else:
                b.next = d
                b = b.next
                d = d.next
        if c:
            b.next = c
        if d:
            b.next = d
        return a.next