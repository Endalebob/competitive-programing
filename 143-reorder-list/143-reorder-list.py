# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        li = []
        ans = head
        while ans:
            li.append(ans.val)
            ans = ans.next
        ans = head
        i = 0
        while ans:
            ans.val = li[i]
            ans = ans.next
            if ans:
                ans.val = li[-1-i]
                ans = ans.next
            i += 1
        """
        Do not return anything, modify head in-place instead.
        """
        