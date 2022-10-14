# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        m = head
        if not m.next:
            return m.next
        while m:
            m = m.next
            i+=1
        c = i//2
        m = head
        for i in range(c-1):
            m = m.next
        m.next =m.next.next
        return head