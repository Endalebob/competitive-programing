# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        li = []
        head = head
        while head:
            li.append(head.val)
            head = head.next
        ans = li[0]
        for i in range(len(li)//2):
            ans = max(ans,li[i]+li[-i-1])
        return ans
        