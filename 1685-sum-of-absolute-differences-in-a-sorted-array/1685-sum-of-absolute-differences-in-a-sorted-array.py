class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prfs = list(accumulate(nums))
        ans = [prfs[-1]-prfs[0]*len(nums)]
        for i in range(1,len(nums)):
            if i < len(nums)-1:
                ans.append((prfs[-1]-prfs[i-1])-nums[i]*(len(nums)-i) + (nums[i]*i - prfs[i-1]))
            else:
                ans.append(nums[i]*i-prfs[i-1])
        return ans
        
        