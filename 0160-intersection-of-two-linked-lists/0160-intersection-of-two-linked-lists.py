# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1,temp2 = headA,headB
        len1,len2 = 0,0
        while temp1:
            len1+=1
            temp1 = temp1.next
        while temp2:
            len2 += 1
            temp2 = temp2.next
        diff = abs(len1-len2)
        if diff>0:
            if len1>len2:
                for i in range(diff):
                    headA = headA.next
            else:
                for i in range(diff):
                    headB = headB.next
        while headB and headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        