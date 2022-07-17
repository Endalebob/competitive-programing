# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1,s2 = '',''
        while l1:
            s1+=str(l1.val)
            l1 = l1.next
        while l2:
            s2+=str(l2.val)
            l2 = l2.next
        ans = str(int(s1)+int(s2))
        hold = ListNode()
        head = hold
        for i in range(len(ans)-1):
            hold.val = ans[i]
            hold.next = ListNode()
            hold = hold.next
        hold.val = ans[-1]
        return head
        