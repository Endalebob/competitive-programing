# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        m = head
        while head.next:
            hold = head
            temp = head.val
            while hold.next:
                if temp > hold.next.val:
                    temp, hold.next.val  = hold.next.val, temp
                hold = hold.next
            head.val = temp
            head = head.next
        return m
                
                