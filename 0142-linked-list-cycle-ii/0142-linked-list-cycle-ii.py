# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isCycle(self,node):
        fast,slow = node,node
        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return fast
        return None
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        check = self.isCycle(head)
        if check:
            ptr1,ptr2 = head,check
            while ptr1 != ptr2:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            return ptr1
        return None