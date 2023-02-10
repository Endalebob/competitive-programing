class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target) or (nums[j] + nums[i] == target):
                    if (nums[i] + nums[j]) == (nums[j] + nums[i]):
                        count+=2
                    else:
                        count+=1
        return count