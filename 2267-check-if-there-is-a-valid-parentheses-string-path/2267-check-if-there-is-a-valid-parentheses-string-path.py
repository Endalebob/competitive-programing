class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        n,m = len(grid),len(grid[0])
        if grid[0][0] != '(' or grid[n-1][m-1] != ')':
            return False
        is_valid = lambda r,c : r<n and c < m
        @lru_cache(None)
        def check(r,c):
            if r == n-1 and c == m - 1:
                return tuple([-1])
            temp = set()
            val = 1 if grid[r][c] == '(' else -1
            if is_valid(r+1,c):
                for i in check(r+1,c):
                    if i + val <= 0:
                        temp.add(i+val)
            if is_valid(r,c+1):
                for i in check(r,c+1):
                    if i + val <= 0:
                        temp.add(i+val)
            return tuple(temp)
        for i in check(0,0):
            if i == 0:
                return True
        return False
            
            