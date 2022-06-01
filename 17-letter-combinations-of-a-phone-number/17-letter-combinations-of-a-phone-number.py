class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2': ['a','b','c'],'3': ['d','e','f'],'4': ['g','h','i'],
            '5': ['j','k','l'],'6': ['m','n','o'],'7': ['p','q','r','s'],
            '8': ['t','u','v'],'9': ['w','x','y','z']}
        ans = []
        dp = {}
        def dfs(idx):
            if idx in dp:
                return dp[idx]
            if idx == len(digits)-1:
                dp[idx] = dic[digits[idx]]
                return dic[digits[idx]]
            temp = []
            for i in dic[digits[idx]]:
                added = dfs(idx+1)
                for j in added:
                    temp.append(i+j)
            dp[idx] = temp
            return temp
        if digits:
            return dfs(0)
            