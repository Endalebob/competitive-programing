class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        gg,ss,ans = 0,0,0
        s.sort()
        g.sort()
        while gg<len(g) and ss<len(s):
            if s[ss]>=g[gg]:
                gg += 1
                ans += 1
            ss += 1
        return ans
            