# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        rotate = deque()
        temp = head
        while temp:
            rotate.append(temp.val)
            temp = temp.next
        if not rotate:
            return
        for i in range(k%len(rotate)):
            rotate.appendleft(rotate.pop())
        temp = head
        for i in rotate:
            temp.val = i
            temp = temp.next
        return head