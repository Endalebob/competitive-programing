class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = set()
        def rec(idx,curr):
            if curr:
                ans.add(curr)
            for i in range(len(idx)):
                val = idx[i]
                new = idx[:i]+idx[i+1:]
                rec(new,curr+val)
        
        rec(list(tiles),"")
        return len(ans)