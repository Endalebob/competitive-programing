class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        def sub(idx,subs):
            if idx == len(nums):
                subset.append(subs.copy())
                return
            subs.append(nums[idx])
            sub(idx+1,subs)
            subs.pop()
            sub(idx+1,subs)
        sub(0,[])
        return subset