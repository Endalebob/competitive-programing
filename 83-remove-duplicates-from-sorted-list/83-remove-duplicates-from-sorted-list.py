# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(None)
        a = ans
        ans.next = head
        if head == None:
            return head
        while head.next:
            if head.val == head.next.val:
                a.next = head.next
                head = head.next
                continue
            a = head
            head = head.next
        return ans.next