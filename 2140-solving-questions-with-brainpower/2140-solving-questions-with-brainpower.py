class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = [-1]*len(questions)
        def dp(idx):
            if idx >= len(questions):
                return 0
            if memo[idx] != -1:
                return memo[idx]
            memo[idx] = max(dp(idx+1),questions[idx][0]+dp(idx+questions[idx][1]+1))
            return memo[idx]
        return dp(0)