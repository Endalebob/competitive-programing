class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cnt_of_odd, cnt_of_even = 0,0
        ans = 0
        for i in arr:
            cnt_of_even += 1
            if i % 2:
                cnt_of_even,cnt_of_odd = cnt_of_odd,cnt_of_even
            ans = (ans + cnt_of_odd) % (10**9+7)
        return ans