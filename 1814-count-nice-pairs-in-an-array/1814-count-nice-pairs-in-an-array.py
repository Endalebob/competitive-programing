class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        ans = 0
        for i in nums:
            new = int(str(i)[::-1])
            new -= i
            ans += dic[new]
            dic[new] += 1
            ans %= (10**9+7)
        return ans