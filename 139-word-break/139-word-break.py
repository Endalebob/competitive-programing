class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # @cache
        dic = {}
        def dp(c_idx,st):
            if c_idx >= len(s):
                return True
            if (c_idx,st) in dic:
                return dic[(c_idx,st)]
            for i in wordDict:
                dic[(c_idx,i)] = False
                if c_idx+len(i) <= len(s):
                    if i == s[c_idx:c_idx+len(i)]:
                        dic[(c_idx,i)]  = dp(c_idx+len(i),i)
                        if dic[(c_idx,i)]:
                            return True
            return dic[(c_idx,i)]
        return dp(0,'')
                        