class Solution:
    def twoSum(self, nums: List[int], k: int) -> List[int]:
        a = 0
        b = len(nums)-1
        ans = []
        while a < b:
            if nums[a] + nums[b]>k:
                b -= 1
            elif nums[a] + nums[b]<k:
                a += 1
            else:
                ans.append(a+1)
                ans.append(b+1)
                a += 1
                b -= 1
        return ans
                