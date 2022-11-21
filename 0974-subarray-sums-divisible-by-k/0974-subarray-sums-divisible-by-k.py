class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref = [0]
        dic = defaultdict(int)
        dic[0] += 1
        ans = 0
        for i in  nums:
            pref.append(pref[-1]+i)
            pref[-1] %= k
            ans += dic[pref[-1]]
            dic[pref[-1]] += 1
        return ans