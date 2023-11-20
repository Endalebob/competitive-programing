class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = 0
        g,p,m = -1,-1,-1
        for i in range(len(garbage)):
            ans += len(garbage[i])
            if 'G' in garbage[i]:
                g = i
            if 'M' in garbage[i]:
                m = i
            if 'P' in garbage[i]:
                p = i
        travel = list(accumulate(travel))
        if m>0:
            ans += travel[m-1]
        if g>0:
            ans += travel[g-1]
        if p>0:
            ans += travel[p-1]
        return ans
                