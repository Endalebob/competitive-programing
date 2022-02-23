# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        monstack = []
        ans = []
        i = 0
        while head:
            hold = [i,head.val]
            ans.append(0)
            while monstack and monstack[-1][1]<head.val:
                ans[(monstack.pop())[0]] = head.val
            monstack.append(hold)
            i += 1
            head = head.next
        return ans
                