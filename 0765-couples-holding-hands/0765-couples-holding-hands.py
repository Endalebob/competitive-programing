class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        ans = 0
        for i in range(1,len(row),2):
            if row[i-1] > row[i]:
                row[i-1],row[i] = row[i],row[i-1]
            if abs(row[i-1]-row[i]) > 1 or row[i] % 2 == 0:
                if row[i-1] % 2:
                    idx = row.index(row[i-1]-1)
                else:
                    idx = row.index(row[i-1]+1)
                row[idx],row[i] = row[i],row[idx]
                ans += 1
        return ans
            