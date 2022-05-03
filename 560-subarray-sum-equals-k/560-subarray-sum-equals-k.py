class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        temp = 0
        count = defaultdict(int)
        ans = 0
        for i,v in enumerate(nums):
            temp += v
            if temp == k:
                ans += 1
            if temp-k in count:
                ans += count[temp-k]
            count[temp] += 1
            
        return ans