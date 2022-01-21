# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li = []
        count = 0
        hold  = head
        while head:
            count += 1
            li.append(head.val)
            head = head.next
        head = hold
        for i in li[::-1]:
            head.val = i
            head = head.next
        return hold