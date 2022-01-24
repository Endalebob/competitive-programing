# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        nl1 = l1
        nl2 = l2
        s=0
        while nl1 or nl2:
            if not nl1:
                nl2.val += s//10
                while nl2.val>=10:
                    if nl2.next != None:
                        nl2.next.val += nl2.val//10
                        nl2.val = nl2.val%10
                        nl2 = nl2.next
                    else:
                        nl2.next = ListNode(val =nl2.val//10, next = None )
                        nl2.val = nl2.val%10
                        return l2
                return l2
            if not nl2:
                nl1.val += s//10
                while nl1.val>=10:
                    if nl1.next != None:
                        nl1.next.val += nl1.val//10
                        nl1.val = nl1.val%10
                        nl1 = nl1.next
                    else:
                        nl1.next = ListNode(val =nl1.val//10, next = None )
                        nl1.val = nl1.val%10
                        return l1
                return l1
            if nl1 and nl2:
                s = nl1.val + nl2.val + s//10
                nl1.val = s%10
                nl2.val = s%10
            if nl1 and nl2:
                if (nl1.next == None and nl2.next == None) and s>9:
                    break
            if nl1:
                 nl1 = nl1.next
            if nl2:
                nl2 = nl2.next
        if nl1:
            nl1.next = ListNode(val =1, next = None )
            nl1.val = nl1.val%10
            return l1
        return l1
            