class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = len(words)
        for i in words:
            if i[:len(pref)] != pref:
                ans -= 1
        return ans