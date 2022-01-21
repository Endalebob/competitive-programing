# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        hold = head
        ii = 0
        while head:
            li = []
            if ii%k == 0:
                temp = head
                kk = head
                for i in range(k):
                    if kk == None:
                        return hold
                    li.append(kk.val)
                    kk = kk.next
                for i in range(k):
                    temp.val = li[-1-i]
                    temp = temp.next
            ii += 1
            head = head.next
        return hold
                
                    