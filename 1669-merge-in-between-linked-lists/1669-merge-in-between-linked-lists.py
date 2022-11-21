# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        copy_l2 = list2
        copy_l1 = list1
        node = ListNode()
        ans = node
        
        na,bb = [],[]
        while copy_l2:
            bb.append(copy_l2.val)
            copy_l2 = copy_l2.next
        while copy_l1:
            na.append(copy_l1.val)
            copy_l1 = copy_l1.next
        new = na[:a] + bb + na[b+1:]
        for i in new:
            ans.next = ListNode(val = i)
            ans = ans.next
        
        
        return node.next