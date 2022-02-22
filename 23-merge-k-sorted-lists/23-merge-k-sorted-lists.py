# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = []
        for i in lists:
            while i:
                heapq.heappush(ans,i.val)
                i = i.next
        list1 = list2 = ListNode()
        while len(ans)>0:
            list2.next = ListNode(heapq.heappop(ans))
            list2 = list2.next
        return list1.next
            
            
                
                
        