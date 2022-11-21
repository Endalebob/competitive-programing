# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        copy_l2 = list2
        copy_l1 = list1
        node = ListNode(next = list1)
        
        i,j = 0,0
        while copy_l2.next:
            copy_l2 = copy_l2.next
        while i != b:
            copy_l1 = copy_l1.next
            i += 1
        copy_l2.next = copy_l1.next
        
        copy_l1 = node
        while j != a:
            copy_l1 = copy_l1.next
            j += 1
        copy_l1.next = list2
        
        return node.next