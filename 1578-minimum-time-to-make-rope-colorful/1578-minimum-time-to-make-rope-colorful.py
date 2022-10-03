class Solution:
    def minCost(self, colors: str, n: List[int]) -> int:
        l,r = 0,1
        ans = 0
        print(colors)
        print(n)
        while r<len(colors):
            if colors[l] == colors[r]:
                if n[l] < n[r]:
                    ans += n[l]
                    l = r
                else:
                    ans += n[r]
            else:
                l = r
            r += 1
        return ans