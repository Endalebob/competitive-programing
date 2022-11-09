class Solution:
    def wordBreak(self, s: str, word: List[str]) -> List[str]:
        # @lru_cache(None)
        wordss = []
        def dp(idx,words):
            if idx == len(s):
                wordss.append(words.strip())
                return
            for i in word:
                if idx + len(i) <= len(s):
                    if s[idx:idx+len(i)] == i:
                        dp(idx+len(i),words+' '+i)
        dp(0,'')
        return wordss