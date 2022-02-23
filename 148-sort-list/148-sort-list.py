# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        l=head
        while head:
            temp.append(head.val)
            head = head.next
        temp.sort()
        ans = l
        i = 0
        while l:
            l.val =temp[i]
            i+=1
            l = l.next
        return ans