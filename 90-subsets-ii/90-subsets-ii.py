class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for i in range(1<<len(nums)):
            temp = []
            for j in range(len(nums)):
                if i & (1<<j):
                    temp.append(nums[j])
            ans.add(tuple(sorted(temp)))
        return ans