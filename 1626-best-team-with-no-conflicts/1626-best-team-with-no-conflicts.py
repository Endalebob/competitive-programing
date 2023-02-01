class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        new = [[i,j] for i,j in zip(ages,scores)]
        new.sort()
        @lru_cache(None)
        def dp(idx,value):
            if idx >= len(scores):
                return 0
            if new[idx][1]  > new[value][1]:
                return max(dp(idx+1,idx)+new[idx][1] ,dp(idx+1,value))
            if (new[idx][1] == new[value][1]) or (new[value][0] == new[idx][0]):
                return dp(idx+1,idx) + new[idx][1]
            return dp(idx+1,value)
        ans = 0
        for i in range(len(scores)):
            ans = max(ans,dp(i,i))
        return ans
                
            