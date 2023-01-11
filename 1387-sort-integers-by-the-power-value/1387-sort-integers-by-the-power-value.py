class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @lru_cache(None)
        def dp(num):
            if num == 1:
                return 0
            if num % 2:
                return 1 + dp(num*3 + 1)
            return 1 + dp(num//2)
        lohi = [i for i in range(lo,hi+1)]
        ans = []
        for i in lohi:
            ans.append(dp(i))
        mapp = defaultdict(list)
        for i in range(len(lohi)):
            mapp[ans[i]].append(lohi[i])
        val = sorted(mapp.keys())
        ret = []
        for i in val:
            for j in mapp[i]:
                ret.append(j)
        return ret[k-1]
        