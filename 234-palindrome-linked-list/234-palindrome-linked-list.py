# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        li = []
        while head:
            li.append(head.val)
            head = head.next
        for i in range(len(li)//2 + 1):
            if li[i] != li[-1-i]:
                return False
        return True