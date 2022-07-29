class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre_sum = []
        tot = 0
        for i in nums:
            tot += i
            pre_sum.append(tot)
        hold = defaultdict(int)
        hold[0] = 1
        ans = 0
        for i in pre_sum:
            ans += hold[i%k] 
            hold[i%k] += 1
        return ans