class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool: 
        def find(i, j):
            if i == j:
                return nums[i]
            return max(nums[i]-find(i+1, j), nums[j]-find(i, j-1))
        return find(0, len(nums)-1) >= 0