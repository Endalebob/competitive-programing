# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        s,f = ans,head
        ans.next = head
        if f == None:
            return f
        c = True
        while f.next:
            m = f.val
            if f.val != f.next.val:
                s.next = f
                s = s.next
                f = f.next
                c = False
            else:
                while f and m == f.val:
                    f = f.next
            if f == None:
                s.next = None
                break
            if f.next == None:
                s.next = f
                
        if c:
            return s.next
        return ans.next
        