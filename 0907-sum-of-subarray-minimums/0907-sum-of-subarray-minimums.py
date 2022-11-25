class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans = 0
        dp = [0]
        mod = 10**9 + 7
        dic = [[arr[0],0]]
        for i in range(len(arr)):
            cnt = 1
            while dic and dic[-1][0] >= arr[i]:
                a,b = dic.pop()
                dp.pop()
                cnt += b
            dic.append([arr[i],cnt])
            if dp:
                dp.append(dp[-1]+arr[i]*cnt)
            else:
                dp.append(arr[i]*cnt)
            ans += dp[-1]
            ans %= mod
        return ans%mod