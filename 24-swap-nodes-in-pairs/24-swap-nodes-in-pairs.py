# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        m = head
        if not head:
            return head
        while head.next:
            count += 1
            if count % 2 == 1:
                head.next.val,head.val = head.val,head.next.val
            head = head.next
        return(m)