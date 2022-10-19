class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        l, r = 1, n * m
        mid = (l + r) // 2
        while l < r:
            cnt = 0
            i = 1
            while i <= n and mid//i:
                cnt += min(m, mid // i)
                i += 1
            if cnt < k:
                l = mid + 1
            else:
                r = mid
            mid = (l + r) // 2
        return mid