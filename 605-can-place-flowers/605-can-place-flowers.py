class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        f.append(0)
        count = 1
        ans = 0
        for i in range(len(f)-1):
            if f[i] == 0:
                count += 1
            else:
                count = 0
            if count == 2 and f[i+1] == 0:
                ans += 1
                count = 0
            if count == 3:
                ans += 1
                count = 0
        return ans >= n
            