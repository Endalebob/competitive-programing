class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stack = [0]
        ans = [0]*len(t)
        for i in range(1,len(t)):
            while stack and t[stack[-1]] < t[i]:
                j = stack.pop()
                ans[j] = i-j
            stack.append(i)
        return ans