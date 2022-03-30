class Solution:
    def count(self,num,mid):
        total = 0
        i = 0
        while len(num)>i:
            if num[i]<=mid:
                total += 1
            i+=1
        return total<=mid
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums)-1
        mid = (right + left)//2
        while left<right:
            if self.count(nums,mid):
                left = mid + 1
            else:
                right = mid
            mid = (right + left)//2 
        return mid
            