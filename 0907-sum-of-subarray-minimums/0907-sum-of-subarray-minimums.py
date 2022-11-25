class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans = 0
        stack = []
        mod = 10**9 + 7
        for i in arr:
            cnt = 1
            while stack and stack[-1][0] >= i:
                val,count,no = stack.pop()
                cnt += count
            if stack:
                curr = stack[-1][-1] + (cnt*i)
                stack.append([i,cnt,curr])
            else:
                stack.append([i,cnt,cnt*i])
            ans += stack[-1][-1]
        return ans % mod