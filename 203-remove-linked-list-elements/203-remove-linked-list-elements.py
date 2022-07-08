# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        newNode = ListNode()
        newNode.next = head
        left = newNode
        right = head
        while right:
            if right.val == val:
                left.next = right.next
            else:
                left = right
            right = right.next
        return newNode.next