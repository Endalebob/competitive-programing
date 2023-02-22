class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = defaultdict(int)
        ans = 0
        for i in time:
            curr = i % 60
            ans += count[(60-curr)%60]
            count[curr] += 1
        return ans
        