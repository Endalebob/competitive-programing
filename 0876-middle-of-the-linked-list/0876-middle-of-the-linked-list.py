# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        b = head
        while a and a.next:
            a = a.next.next
            b = b.next
            if a == None or a.next == None:
                break
        return b