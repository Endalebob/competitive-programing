# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        ans = [temp[-1]]
        mi = temp[-1]
        for i in range(len(temp)-2,-1,-1):
            if temp[i] >= mi:
                mi = temp[i]
                ans.append(mi)
        ret = ListNode()
        c = ret
        ans = ans[::-1]
        cnt = 1
        for i in ans:
            c.val = i
            if cnt == len(ans):
                return ret
            c.next = ListNode()
            c = c.next
            cnt += 1
        return ret
            