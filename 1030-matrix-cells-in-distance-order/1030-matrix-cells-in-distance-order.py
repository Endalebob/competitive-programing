class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        ans = defaultdict(list)
        for i in range(rows):
            for j in range(cols):
                dis = abs(i-rCenter)+abs(j-cCenter)
                ans[dis].append([i,j])
        anss = sorted(ans)
        ret = []
        for i in anss:
            ret += ans[i]
        return ret