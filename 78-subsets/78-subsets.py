class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(1<<len(nums)):
            temp = []
            for j in range(len(nums)):
                if i &(1<<j):
                    temp.append(nums[j])
            ans.append(temp)
        return ans