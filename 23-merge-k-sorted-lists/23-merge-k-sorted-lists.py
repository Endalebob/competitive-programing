# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = []
        correct = ret = ListNode()
        for i in lists:
            while i:
                ans.append(i.val)
                i = i.next
        ans.sort()
        for i in ans:
            ret.next = ListNode(val = i)
            ret = ret.next
        return correct.next