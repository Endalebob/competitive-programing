class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        count = Counter(letters)
        val = {}
        for i in range(26):
            val[chr(ord('a')+i)] = score[i]
        @lru_cache(None)
        def dp(idx,selected):
            if idx >= len(words):
                return 0
            nCount = Counter(words[idx])
            flag = True
            for i in nCount:
                if nCount[i] > count[i]:
                    flag = False
                    break
            ans = dp(idx+1,selected)
            if flag:
                add = 0
                m = list(selected)
                m.append(idx)
                
                for i in nCount:
                    add += val[i]*nCount[i]
                    count[i] -= nCount[i]
                ans = max(ans,dp(idx+1,tuple(m))+add)
                for i in nCount:
                    count[i] += nCount[i]
            return ans
        return dp(0,())
        