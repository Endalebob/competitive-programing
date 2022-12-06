# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, node: Optional[ListNode]) -> Optional[ListNode]:
        if not node or not node.next:
            return node
        lis = [node.val]
        while node := node.next:
                lis.append(node.val)
        odd,even = ListNode(),ListNode()
        od,eve = odd,even
        for i in range(0,len(lis),2):
            odd.val = lis[i]
            if i+1 < len(lis):
                even.val = lis[i+1]
            if i == len(lis)-1:
                odd.next = eve
                return od
            if i < len(lis)-3:
                odd.next,even.next = ListNode(),ListNode()
                odd,even = odd.next,even.next
            elif i < len(lis)-2:
                odd.next=ListNode()
                odd = odd.next
        odd.next = eve
        return od
            