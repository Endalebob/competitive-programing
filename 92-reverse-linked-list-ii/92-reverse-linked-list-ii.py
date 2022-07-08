# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp = head
        nums = []
        while temp:
            nums.append(temp.val)
            temp = temp.next
        show = []
        for i in range(right-1,left-2,-1):
            show.append(nums[i])
        nums[left-1:right] = show
        temp = head
        for i in nums:
            temp.val = i
            temp = temp.next
        return head
        