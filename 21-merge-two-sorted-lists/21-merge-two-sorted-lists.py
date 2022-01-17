# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mm = ListNode()
        ans = mm
        while list1 or list2:
            if list1 == None:
                ans.next = list2
                list2 = list2.next
            elif list2 == None:
                ans.next = list1
                list1 = list1.next
            elif list1.val<list2.val:
                ans.next = list1
                list1 = list1.next
            else:
                ans.next = list2
                list2 = list2.next
            ans = ans.next
        return mm.next