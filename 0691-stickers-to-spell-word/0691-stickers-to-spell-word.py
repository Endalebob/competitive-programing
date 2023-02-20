class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        def add_sticker(sticker_counts, s):
            for char in sticker_counts:
                s = s.replace(char, '', sticker_counts[char])  
            return s

        @lru_cache(None)
        def dfs(s):
            if not s: 
                return 0
            res = float('inf')
            for sticker_counts in stickers:
                if s[0] not in sticker_counts: 
                    continue
                new_s = add_sticker(sticker_counts, s)
                res = min(res, 1 + dfs(new_s))
            return res

        # Convert each sticker into a Counter object
        stickers = [Counter(s) for s in stickers]
        res = dfs(target) 
        return res if res != float('inf') else -1
