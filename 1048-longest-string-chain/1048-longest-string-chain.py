class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x:len(x))
        possible_case = defaultdict(set)
        for i in words:
            for j in range(len(i)):
                possible_case[i].add(i[:j]+i[j+1:])
        @lru_cache(None)
        def dp(prev,idx):
            if idx >= len(words):
                return 0
            if prev in possible_case[words[idx]]:
                return 1 + max(dp(words[idx],idx+1),dp(prev,idx+1)-1)
            return dp(prev,idx+1)
        ans = 0
        for i in range(len(words)):
            ans = max(ans,1 + dp(words[i],i+1))
        return ans