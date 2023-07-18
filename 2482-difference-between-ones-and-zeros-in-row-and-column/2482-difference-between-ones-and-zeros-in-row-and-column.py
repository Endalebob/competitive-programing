class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        zerosR = {}
        zerosC = defaultdict(int)
        onesR = {}
        onesC = defaultdict(int)
        n,m = len(grid),len(grid[0])
        for i in range(n):
            one = grid[i].count(1)
            zerosR[i] = m-one
            onesR[i] = one
        for i in range(m):
            for j in range(n):
                if grid[j][i]:
                    onesC[i] += 1
                else:
                    zerosC[i] += 1
        for i in range(n):
            for j in range(m):
                grid[i][j] = onesR[i]+onesC[j] - zerosR[i] - zerosC[j]
        return grid