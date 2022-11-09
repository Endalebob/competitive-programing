class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count_of_nums = Counter(nums)
        ans = [0,0]
        for i in range(1,len(nums)+1):
            if i not in count_of_nums:
                ans[1] = i
            elif count_of_nums[i] == 2:
                ans[0] = i
        return ans