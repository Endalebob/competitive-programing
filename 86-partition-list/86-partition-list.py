# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp = head
        nums = []
        while temp:
            nums.append(temp.val)
            temp = temp.next
            
        start = 0
        for i in range(len(nums)):
            if nums[i]==x:
                start = i
                break
        hold = []
        cc = nums[::]
        qero = 0
        for i in range(len(nums)):
            if nums[i]<x:
                cc.pop(i-qero)
                qero+=1
                hold.append(nums[i])
        nums = cc
        for i in range(len(nums)):
            if nums[i]>=x:
                nums[i:i] = hold
                break
        temp = head
        for i in nums:
            temp.val = i
            temp = temp.next
        return head