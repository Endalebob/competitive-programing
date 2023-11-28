class Solution:
    def numberOfWays(self, corridor: str) -> int:
        s_count = corridor.count('S')
        if not s_count or s_count % 2:
            return 0
        i = len(corridor)-1
        cnt2 = 0
        ans = 1
        while i >= 0:
            mul = 1
            while cnt2 and cnt2 % 2 == 0 and corridor[i] == 'P':
                mul += 1
                i -= 1
            if cnt2 % 2 == 0:
                ans *= mul
            if corridor[i] == 'S':
                cnt2 += 1
            if cnt2 == s_count:
                break
            i -= 1
            ans %= (10**9+7)
        return ans % (10**9+7)
                