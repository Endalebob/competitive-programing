# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pree = ListNode(None)
        pre = pree
        pree.next = head
        ne = head
        count = 0
        while ne:
            count += 1
            ne = ne.next
        ne = head
        for i in range(count):
            if  i==count - n:
                pre.next = ne.next
            else:
                pre = ne
                ne = ne.next
        return pree.next
        