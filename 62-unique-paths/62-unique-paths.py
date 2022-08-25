class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dic = {}
        def rec(r,d):
            if r == m-1 or d == n-1:
                return 1
            if (r,d) in  dic:
                return dic[(r,d)]
            dic[(r,d)] = rec(r+1,d) + rec(r,d+1)
                
            return dic[(r,d)]
        return rec(0,0)