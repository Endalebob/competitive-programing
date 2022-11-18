class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        track = 0
        # dic[track] += 1
        ans = 0
        for i in nums:
            track += i
            if track == k:
                ans += 1
            ans += dic[track-k]
            dic[track] += 1
        return ans