class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd = 0
        even = 0
        ans = 0
        mod = 10**9+7
        for i in arr:
            if i%2:
                odd,even = even,odd
                odd += 1
            else:
                even += 1
            ans += odd
        return ans%mod
                
        