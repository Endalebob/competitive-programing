class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursive(nums, perm=[], res=[]):
            if not nums: # -- NOTE [1] 
                res.append(perm[::])

            for i in range(len(nums)): # [1,2,3]
                newNums = nums[:i] + nums[i+1:]
                perm.append(nums[i])
                recursive(newNums, perm, res)
                perm.pop()
            return res

        return recursive(nums)