class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        ans = len(nums)
        val = defaultdict(int)
        maxValue = limit+1
        for i in range(len(nums)//2):
            val[nums[i]+nums[-i-1]] += 1
            val[nums[i]+nums[-i-1]+1] -= 1
            val[min(nums[i],nums[-i-1])+1] += 1
            val[max(nums[i],nums[-i-1])+limit+1] -= 1
            maxValue = max(maxValue,max(nums[i],nums[-i-1])+limit+1)
        curr = ans
        for i in range(1,maxValue):
            curr -= val[i]
            ans = min(ans,curr)
        return ans