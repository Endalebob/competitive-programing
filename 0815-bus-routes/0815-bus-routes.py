class Solution:
    def numBusesToDestination(self, rts: List[List[int]], src: int, tgt: int) -> int:
        g = defaultdict(list)
        for i, r in enumerate(rts):
            p = r[0]
            for j in range(1, len(r)):
                g[p].append((r[j], i))
                g[r[j]].append((p, i))
                p = r[j]

        h = [(0, 0, src, None)]
        v = set()
        c = 1
        while len(h) > 0:
            bc, o, cur, prev = heapq.heappop(h)
            if cur == tgt:
                return bc
            v.add((cur, prev))
            for nxt, cb in g[cur]:
                nbc = bc + (1 if cb != prev else 0)
                if (nxt, cb) not in v:
                    heapq.heappush(h, (nbc, c, nxt, cb))
                    c += 1
        return -1       