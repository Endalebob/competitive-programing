class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic = defaultdict(int)
        dic[0] += 1
        ans = 0
        curr = 0
        for i in nums:
            curr += i
            ans += dic[curr-goal]
            dic[curr] += 1
        return ans