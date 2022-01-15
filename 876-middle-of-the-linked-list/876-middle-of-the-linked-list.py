# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        m = 0
        cc = head
        while head.next != None:
            m += 1
            head = head.next
        if m == 0:
            return head
        c=0
        a = (m//2)+(m%2)
        head = cc
        while a>0:
            c = head.next
            head = head.next
            a-=1
        return c